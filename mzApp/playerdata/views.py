from django.shortcuts import render
from .forms import PlayerDataForm

def input_data(request):
    if request.method == 'POST':
        form = PlayerDataForm(request.POST)
        if form.is_valid():
            data_input = form.cleaned_data['data_input']
            players = parse_input_data(data_input)
            return render(request, 'playerdata/table.html', {'players': players})
    else:
        form = PlayerDataForm()

    return render(request, 'playerdata/input.html', {'form': form})

def parse_input_data(data_input):
    lines = data_input.strip().split('\n')
    players = []
    index = 0

    while index < len(lines):
        try:
            number = lines[index].strip()
            name = lines[index + 1].strip()
            value = lines[index + 2].strip()
            salary = lines[index + 3].strip()
            attributes = lines[index + 4].strip().split()

            if len(attributes) == 15:  # Adjust based on the exact number of attributes
                player = {
                    'number': number,
                    'name': name,
                    'value': value,
                    'salary': salary,
                    'age': attributes[0],
                    'born': attributes[1],
                    'speed': attributes[2],
                    'stamina': attributes[3],
                    'play_intelligence': attributes[4],
                    'passing': attributes[5],
                    'shooting': attributes[6],
                    'heading': attributes[7],
                    'keeping': attributes[8],
                    'ball_control': attributes[9],
                    'tackling': attributes[10],
                    'aerial_passing': attributes[11],
                    'set_plays': attributes[12],
                    'experience': attributes[13],
                    'form': attributes[14],
                }
                players.append(player)
            index += 5  # Move to the next player's data
        except IndexError:
            break  # Stop if there's incomplete data

    return players

def update_maxings(request):
    players = PlayerDataForm.objects.all()
    if request.method == 'POST':
        for player in players:
            for attr in player.get_attributes():
                checkbox_name = f"maxed_{player.id}_{attr[0]}"
                if checkbox_name in request.POST:
                    player.mark_as_maxed(attr[0])  # Implement this method to handle maxed state

    return render(request, 'table.html', {'players': players})
