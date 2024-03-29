from django.shortcuts import render

characters_info = [
    {
        "slug": "jack-oneill",
        "image": "jack.jpg",
        "name": "Jack O'Neill",
        "planet": "Terre",
        "excerpt": "Jack O'Neill est un personnage capable de plaisanter dans les pires moments.",
        "citation": "O'Neill... avec deux l",
        "description": "Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo, consequuntur modi. Debitis accusamus sit id. Cum consequatur ullam reiciendis laboriosam, eius illum iure quia, inventore tempore accusamus accusantium reprehenderit necessitatibus deserunt dolore! Quidem ipsa rerum consectetur temporibus dolor doloribus, officiis est eligendi reiciendis accusantium sed mollitia esse nam suscipit aperiam maxime placeat illum vel aliquid? Inventore enim, officia, doloremque minus itaque commodi, incidunt dolorum tempora libero possimus assumenda eveniet asperiores."
    },
    {
        "slug": "samantha-carter",
        "image": "samantha.jpg",
        "name": "Samantha Carter",
         "planet": "Terre",
        "citation": "Je suis officier de l'armée de l'air, comme vous, mon colonel. Et le fait que mes organes de reproduction soient situés à l'intérieur de mon corps, ne veut pas dire que je vous suis inférieure, mon colonel...",
        "excerpt": "Samantha est une scientifique soldat hors pair",
        "description": "Smantha Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo, consequuntur modi. Debitis accusamus sit id. Cum consequatur ullam reiciendis laboriosam, eius illum iure quia, inventore tempore accusamus accusantium reprehenderit necessitatibus deserunt dolore! Quidem ipsa rerum consectetur temporibus dolor doloribus, officiis est eligendi reiciendis accusantium sed mollitia esse nam suscipit aperiam maxime placeat illum vel aliquid? Inventore enim, officia, doloremque minus itaque commodi, incidunt dolorum tempora libero possimus assumenda eveniet asperiores."
    },
    {
        "slug": "daniel-jackson",
        "image": "daniel.jpg",
        "name": "Daniel Jackson",
         "planet": "Terre",
        "citation": "Ça ne vous est jamais arrivé de ressentir quelque chose de totalement contraire à la logique, et qui s'avère pourtant exact ?",
        "excerpt": "Egyptologue, polyglotte et en pleine réflexion",
        "description": "Daniel Lorem ipsum, dolor sit amet consectetur adipisicing elit. Explicabo, consequuntur modi. Debitis accusamus sit id. Cum consequatur ullam reiciendis laboriosam, eius illum iure quia, inventore tempore accusamus accusantium reprehenderit necessitatibus deserunt dolore! Quidem ipsa rerum consectetur temporibus dolor doloribus, officiis est eligendi reiciendis accusantium sed mollitia esse nam suscipit aperiam maxime placeat illum vel aliquid? Inventore enim, officia, doloremque minus itaque commodi, incidunt dolorum tempora libero possimus assumenda eveniet asperiores."
    }
]

# Create your views here.


def homepage(request):
    return render(request, 'characters/index.html')


def characters(request):
    return render(request, 'characters/characters-list.html', { 
        "characters" : characters_info 
    })


def characters_details(request, slug):
    character_to_display = next(character for character in characters_info if character['slug'] == slug)
    return render(request, 'characters/character-details.html', { 
        "character" : character_to_display
    })
