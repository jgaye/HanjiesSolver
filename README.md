HanjiesSolver
=============

22/07/14

M: texte écrit par Marvin
P: texte écris par Pucci

M: Utilisons ce doc comme un log pour l'instant = les nouveaux commentaires vont au début (en haut) du doc, avec la date.

Ce projet a pour but de créer un solveur de Hanjies (ou Picross, ou logigramme) en collaboration avec mon bon ami Pucci.
Mes motivations sont d'utiliser ce projet pour apprendre un nouveau langage; réaliser un projet de bout en bout et en collaboration avec Pucci, ce qui pourra amener a plus de collaboration; et coder un programme utilisant de l'algorithmie un peu plus intelligente que ce que j'ai fait jusqu'a présent.
Mes objectifs sont à deux niveaux : Obtenir un programme qui marche bien, optimisé et pas trop dur à maanier pour une utilisation personnelle; meilleur encore serait d'en faire une app mobile, que l'on supporterait ou non (plutôt non aujourd'hui).

A faire/ décider:

-Quel langage utiliser ? 
Tant que ce n'est pas du Java je suis content. Nous devrions nous poser des questions sur la complexité des algos et ce qu'il faudra garder en mémoire.

-Comment collaborer à deux / comment faire la division du travail ?
Pour l'instant je pense qu'il y a assez à faire pour qu'on choisisse chacun les fonctionnalités qui nous interessent personnelement et qu'on ait nos propres branches séparrées. Il faut quand même qu'on reflechisse à l'archi globale un peu avant.

-Reflexion sur "l'archi" generale
Je suis d'avis de separer la reflexion entre l'input des données, la présentation (output 'graphique') et l'algorithmie qui va résoudre le picross.
Du coup, le premier jeu de fonctionnalités serait pour moi:
1. Input de données 
2. Traduction entre l'input et les objets nécessaires pour lancer les algos
3. Tous les algos de résolution (grosse partie à mon avis)
3 bonus. optimisation des algos
4. Output en temps réel ou non
4 bonus. Output graphique

J'ai des idées sur chacune de ces parties mais je pense qu'on devrait lancer des threads pour chacune de ces fonctionnalités dans la ML d'anord.

Pour le 3. je vois deux façons de faire et je prefererais clairement la premiere mais ça peut etre tres dur:
1. On tatonne pour trouver les méthodes de résolutions, cad qu'on implement ce qu'on sait sur la résolution petit a petit mais de façon plus naturelle, plus orgnanique. Ce la veut dire qu'on aura du mal a résoudre des Picross au début, puis on arrivera a en résoudre de plus en plus mais qu'il faudra ensuite revenir sur l'étape d'optimisation.
2. On récupère la théorie du Picross déjà toute faite sur Wikipedia ou Reddit et on implemente toutes les m´thodes de résolution.

Je préfère la 1 car on doit mener la reflexion nous même et résoudre nos impasses par test et erreurs. Bref un vrai travail d'ingénieur =)
