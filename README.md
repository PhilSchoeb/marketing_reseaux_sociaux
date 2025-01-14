# marketing_reseaux_sociaux
Résolution algorithmique d'un problème de marketing de réseaux sociaux - Introduction à l'algorithmique (IFT2125).

Utilisation d'un algorithme glouton afin de trouver un ensemble d'influenceurs qui couvre tous les auditeurs. Le fichier "instance.txt" est un exemple d'input.

### Discussion

L'approche choisie est de traiter chaque influenceur comme un élément dans une liste. Chaque influenceur et ses auditeurs sont contenus dans un tableau, qui sont des éléments de la liste. L'algorithme vorace sélectionne à chaque itération d'influenceur celui qui a le plus grand nombre d'auditeurs. On ajoute l'influenceur en sortie s'il couvre au moins un auditoire qui n'a pas encore été traité par un influenceur précédemment choisi. Sinon, on n'ajoute pas cet influenceur dans la réponse en sortie. Au final, on retourne la liste des influenceurs choisis.

La fonction "sélection" de l'algorithme glouton, qui est la fonction {\textit max()}, est d'un ordre de complexité $O(n)$ , où $n$ est le nombre d'influenceurs, car elle compare la longueur de chaque élément de la liste pour déterminer lequel est le plus long. Cette fonction max est appelée n fois et cela rend cette partie de l'algo en $O(n^2)$. Soit a le nombre total d'auditeurs, on compare n fois si l'influenceur précédemment sélectionné couvre déjà tous les auditeurs du prochain influenceur potentiel. Ceci se fait en $O(n\cdot a)$. Ainsi, la complexité théorique est de $O(n^2+n\cdot a)$ dans le pire cas, où chaque élément de la liste est aussi longue l'une comparée à l'autre, et aucun n'influenceur n'a d'auditeurs communs entre eux.

De manière empirique, on compare en entrée le fichier instance\_p100\_i10.txt, ainsi que instance\_p1000\_i100.txt qui contient 10 fois plus d'influenceurs, c'est-à-dire d'un facteur de $n^2$. Le temps d'exécution du fichier instance\_p100\_i10.txt est en moyenne de 0.001 seconde, alors que celui de instance\_p1000\_i100.txt est d'environ 0.092 seconde. Ce temps s'approche du carré du temps d'exécution du premier fichier, ce qui confirme empiriquement que notre algorithme s'exécute en $O(n^2)$.

02/2023
