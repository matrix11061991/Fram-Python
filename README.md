```sh
  ______                                           _            _____       _   _                 
 |  ____|                                         | |          |  __ \     | | | |                
 | |__ _ __ __ _ _ __ ___   _____      _____  _ __| | __       | |__) |   _| |_| |__   ___  _ __  
 |  __| '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /       |  ___/ | | | __| '_ \ / _ \| '_ \ 
 | |  | | | (_| | | | | | |  __/\ V  V / (_) | |  |   <        | |   | |_| | |_| | | | (_) | | | |
 |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\       |_|    \__, |\__|_| |_|\___/|_| |_|
                                                                       __/ |                      
                                                                      |___/                       
```
# Fiche d'activité pratique sur quelques framework Python:
```sh
  ____        _   _   _      
 |  _ \      | | | | | |     
 | |_) | ___ | |_| |_| | ___ 
 |  _ < / _ \| __| __| |/ _ \
 | |_) | (_) | |_| |_| |  __/
 |____/ \___/ \__|\__|_|\___|
```                          
- [Bottle](Prj-Bottle.md)
  est un micro-framework web pour le langage de programmation Python. Il est conçu pour être simple, léger et facile à utiliser, tout en offrant les fonctionnalités nécessaires pour développer des applications web de petite à moyenne envergure.  Voici quelques caractéristiques et utilités de Bottle :
  - **Micro-framework :** Bottle est considéré comme un micro-framework car il fournit le strict nécessaire pour développer des applications web. Il n'inclut pas de composants excessifs, ce qui le rend simple et facile à comprendre.
  - **Routing :** Bottle permet de définir des routes URL facilement en associant des fonctions à des URL spécifiques. Cela simplifie la création de points de terminaison pour votre application.
  - **Templates :** Bottle propose un moteur de modèle intégré qui permet de générer des pages HTML dynamiques en utilisant des templates. Il facilite la création de vues pour vos applications.
  - **Serveur de développement intégré :** Bottle inclut un serveur web de développement, ce qui signifie que vous pouvez démarrer rapidement votre application sans avoir besoin d'un serveur web externe dans un environnement de développement.
  - **Aucune dépendance externe :** Bottle ne nécessite pas l'installation d'autres bibliothèques ou composants tiers, ce qui facilite son utilisation et son déploiement.
  - **Simple à intégrer :** En raison de sa nature légère, Bottle est facile à intégrer avec d'autres bibliothèques et frameworks Python. Vous pouvez l'utiliser pour construire des composants web dans le cadre de projets plus importants.
  - **Applications RESTful :** Bottle est souvent utilisé pour créer des applications RESTful, où les routes correspondent à des opérations sur des ressources.
```sh
   _____ _                          _____       
  / ____| |                        |  __ \      
 | |    | |__   ___ _ __ _ __ _   _| |__) |   _ 
 | |    | '_ \ / _ \ '__| '__| | | |  ___/ | | |
 | |____| | | |  __/ |  | |  | |_| | |   | |_| |
  \_____|_| |_|\___|_|  |_|   \__, |_|    \__, |
                               __/ |       __/ |
                              |___/       |___/ 
```
- [CherryPy](Prj-CherryPy.md)
  est un framework web pour le langage de programmation Python. Il offre une approche modulaire pour le développement d'applications web, facilitant la création de serveurs web et d'applications avec une architecture orientée objet. Voici quelques caractéristiques et utilisations de CherryPy :
  - **Serveur Web intégré :** CherryPy inclut un serveur web intégré, ce qui signifie que vous pouvez exécuter votre application CherryPy sans avoir besoin d'un serveur web externe. Cela simplifie le processus de développement et de déploiement.
  - **Approche orientée objet :** CherryPy adopte une approche orientée objet pour la construction d'applications web. Les fonctionnalités et les comportements de l'application sont organisés en classes, ce qui facilite la gestion de la complexité.
  - **Facilité d'utilisation :** CherryPy est conçu pour être simple à utiliser. La configuration de l'application se fait généralement en utilisant des décorateurs et des classes Python, ce qui peut rendre le code plus lisible et modulaire.
  - **Gestion des sessions :** CherryPy propose une gestion intégrée des sessions, ce qui simplifie la gestion de l'état de l'application entre différentes requêtes HTTP.
  - **Intégration avec d'autres technologies :** CherryPy peut être intégré avec d'autres bibliothèques et outils Python. Il peut être utilisé avec des moteurs de template tels que Jinja2 ou Mako, et il prend en charge différentes technologies de middleware.
  - **Flexibilité :** CherryPy offre une certaine flexibilité dans la façon dont vous organisez votre application et gère les requêtes HTTP. Cela peut être particulièrement utile pour des projets nécessitant une personnalisation approfondie.
  - **Déploiement sur différents serveurs :** Bien que CherryPy dispose de son propre serveur web intégré, il peut également être déployé sur des serveurs web plus robustes tels que Apache ou Nginx.
```sh
  _____  _                         
 |  __ \(_)                        
 | |  | |_  __ _ _ __   __ _  ___  
 | |  | | |/ _` | '_ \ / _` |/ _ \ 
 | |__| | | (_| | | | | (_| | (_) |
 |_____/| |\__,_|_| |_|\__, |\___/ 
       _/ |             __/ |      
      |__/             |___/       
```
- [Django](Prj-Django.md)  est un framework web open source écrit en Python qui facilite le développement rapide d'applications web robustes et maintenables. Il suit le modèle architectural MVC (Modèle-Vue-Contrôleur) ou, plus précisément, le modèle MTV (Modèle-Template-Vue), propre à Django. Voici quelques caractéristiques et utilisations clés de Django :
  - **Développement rapide :** L'un des principaux objectifs de Django est de faciliter le développement rapide d'applications web. Il fournit un ensemble de fonctionnalités prêtes à l'emploi pour gérer des tâches courantes, permettant aux développeurs de se concentrer sur la logique spécifique de leur application.
  - **Architecture MTV :** Django utilise le modèle MTV, où le Modèle représente la logique métier et les données, le Template gère l'interface utilisateur, et la Vue gère l'interaction entre le Modèle et le Template. Cela favorise la séparation des préoccupations et la maintenabilité du code.
  - **ORM (Object-Relational Mapping) :** Django inclut un ORM puissant qui permet aux développeurs de travailler avec des bases de données relationnelles en utilisant des objets Python au lieu de SQL brut. Cela simplifie la manipulation des données et rend le code plus portable entre différents systèmes de gestion de bases de données.
  - **Administration automatique :** Django fournit une interface d'administration automatique générée à partir de vos modèles de base de données. Cela facilite la gestion et la visualisation des données sans avoir à créer une interface d'administration personnalisée.
  - **Sécurité intégrée :** Django intègre de nombreuses fonctionnalités de sécurité par défaut, telles que la protection contre les attaques CSRF (Cross-Site Request Forgery), l'échappement automatique des données pour éviter les attaques XSS (Cross-Site Scripting), etc.
  - **Système de gestion des URL :** Django propose un système de gestion des URL puissant et flexible, permettant de définir des schémas d'URL lisibles et modulaires.
  - **Extensibilité :** Django est extensible avec des modules tiers (applications) qui peuvent être réutilisés dans différentes applications. Cela favorise la modularité et la réutilisabilité du code.
  - **Communauté active :** Django bénéficie d'une communauté de développeurs active, avec une documentation exhaustive, des plugins tiers, et un écosystème de soutien.

```sh
  ______ _           _    
 |  ____| |         | |   
 | |__  | | __ _ ___| | __
 |  __| | |/ _` / __| |/ /
 | |    | | (_| \__ \   < 
 |_|    |_|\__,_|___/_|\_\
                          
```
- [Flask](Prj-Flask.md)  est un framework web léger et open source écrit en Python. Conçu pour être simple et extensible, Flask permet de développer rapidement des applications web avec une grande flexibilité. Voici quelques caractéristiques et utilisations clés de Flask :
  - **Micro-framework :** Flask est souvent appelé un "micro-framework" parce qu'il offre le strict nécessaire pour développer des applications web. Cela signifie qu'il n'inclut que le minimum vital pour maintenir la simplicité et permettre aux développeurs d'ajouter des fonctionnalités spécifiques selon leurs besoins.
  - **acilité d'utilisation :** Flask est connu pour sa facilité d'utilisation. Il propose une syntaxe simple et intuitive qui permet aux développeurs de se concentrer sur la logique métier plutôt que sur des détails complexes de configuration.
  - **Flexibilité :** Flask offre une grande flexibilité dans la manière dont vous structurez votre application. Il ne force pas une structure particulière et vous permet de choisir les bibliothèques et les outils que vous souhaitez utiliser.
  - **Extensibilité :** Bien que Flask soit léger, il est extensible. Vous pouvez ajouter des fonctionnalités supplémentaires grâce à des extensions Flask ou intégrer des bibliothèques tierces pour répondre à des besoins spécifiques.
  - **Jinja2 pour les templates :** Flask utilise le moteur de templates Jinja2, ce qui permet de générer des pages HTML de manière dynamique en intégrant des variables et des structures de contrôle dans les templates.
  - **Système de routage :** Flask propose un système de routage simple pour définir des routes URL et associer des fonctions de gestion à ces routes. Cela permet de gérer facilement les différentes pages de l'application.
  - **Intégration avec Werkzeug :** Flask s'appuie sur Werkzeug, une bibliothèque WSGI (Web Server Gateway Interface) pour gérer les aspects bas niveau des connexions HTTP. Cela garantit une gestion robuste des requêtes et des réponses.
  - **Serveur de développement intégré :** Flask inclut un serveur web de développement pour faciliter le processus de développement et de test.
  - **Applications RESTful :** Flask est souvent utilisé pour développer des applications RESTful, où les routes correspondent à des opérations sur des ressources.
```sh
  _____                           _     _ 
 |  __ \                         (_)   | |
 | |__) |   _ _ __ __ _ _ __ ___  _  __| |
 |  ___/ | | | '__/ _` | '_ ` _ \| |/ _` |
 | |   | |_| | | | (_| | | | | | | | (_| |
 |_|    \__, |_|  \__,_|_| |_| |_|_|\__,_|
         __/ |                            
        |___/                             
```
- [Pyramid](Prj-Pyramid.md)  st un framework web open source écrit en Python qui se situe entre les frameworks web micro et les frameworks web full-stack. Il est conçu pour être souple, extensible et adapté à une variété de types d'applications, du plus petit projet au plus grand. Voici quelques caractéristiques et utilisations clés de Pyramid :
  - **Flexibilité :** L'une des caractéristiques principales de Pyramid est sa grande flexibilité. Il n'impose pas de structure particulière à votre application, vous permettant de choisir comment organiser votre code et quelles bibliothèques utiliser.
  - **Évolutivité :** Pyramid est capable de gérer des applications de toutes tailles, des plus petites aux plus grandes. Il offre des outils pour structurer votre application de manière modulaire afin de faciliter la gestion de la complexité à mesure que votre projet évolue.
  - **Modularité :** Pyramid est basé sur le concept de modularité. Vous pouvez ajouter des fonctionnalités à votre application en utilisant des modules (ou "packages") et des composants réutilisables.
  - **Choix de moteurs de templates :** Pyramid n'impose pas un moteur de templates particulier. Vous pouvez choisir le moteur de templates qui convient le mieux à votre projet, que ce soit Jinja2, Mako, ou tout autre moteur compatible.
  - **Authentification et autorisation :** Pyramid fournit des outils pour gérer l'authentification et l'autorisation dans votre application. Vous pouvez implémenter des systèmes d'authentification personnalisés et définir des politiques d'autorisation complexes.
  - **Intégration avec des systèmes existants :** Pyramid peut être utilisé pour construire de nouvelles applications ou pour ajouter des fonctionnalités à des applications existantes. Il offre une flexibilité d'intégration avec des systèmes et des bibliothèques tiers.
  - **Système de routage :** Pyramid propose un système de routage flexible qui vous permet de définir des routes URL et d'associer des vues à ces routes. Cela facilite la gestion des requêtes HTTP.
  - **Prise en charge de WebSocket :** Pyramid prend en charge WebSocket, ce qui permet de construire des applications temps réel et interactives.
  - **Documentation approfondie :** Pyramid dispose d'une documentation approfondie qui facilite l'apprentissage et le développement avec le framework.




