# lider-ahenk-user-privilege-plugin

**Lider Ahenk** is an open source project which provides solutions to manage, monitor and audit unlimited number of different systems and users on a network.

Lider Ahenk user-privilege plugin. **TODO**

This documentation **only** covers plugin related topics. To learn about core projects, please see other lider ahenk projects section.


> We use Eclipse for Lider and Lider Console related development. See these documentation [here](https://github.com/Pardus-Kurumsal/lider-console/wiki/01.-Setup-Development-Environment) and [here](https://github.com/Pardus-Kurumsal/lider/wiki/01.-Setup-Development-Environment) to setup Eclipse IDE with Lider and Lider Console projects imported.

1. Clone the plugin project by running `git clone https://github.com/Pardus-Kurumsal/lider-ahenk-user-privilege-plugin.git`.
2. Open Eclipse and import the plugin project into Eclipse as 'Existing Maven Projects'.


1. Navigate to project root directory and run `mvn clean install -DskipTests`.


Plugin project consists of three sub-modules (for **Lider**, **Lider Console** and **Ahenk**). Each sub-module is its own plugin that needs to be handled separately. Below is an explanation regarding how to run each sub-module:


> **Prerequisite**: Make sure you have a running Karaf container on which Lider core components installed. See [this documentation](https://github.com/Pardus-Kurumsal/lider/wiki/02.-Building-&-Running) for how to run Lider on Karaf container.

1. Type `feature:repo-add  mvn:tr.org.liderahenk/lider-user-privilege-feature/1.0.0/xml/features` on Karaf shell. This will add plugin repository to the Karaf instance.
2. Again on Karaf shell, run `feature:install lider-user-privilege` to install and run plugin bundles.
3. Use `log:tail` and `plugin:list` commands to ensure the plugin is installed and working properly.


> **Prerequisite**: Make sure you have a running Lider Console application. See [this documentation](https://github.com/Pardus-Kurumsal/lider-console/wiki/02.-Building-&-Running) for how to run Lider Console on Eclipse.

1. Open Eclipse, go to 'Run --> Debug Configurations' menu and on 'Plugins' tab, select _lider-console-user-privilege_
2. Click 'Add Required Plugins' button to add any plugins the project depend on.
3. Finally you can run Lider Console as explained in its [documentation](https://github.com/Pardus-Kurumsal/lider-console/wiki/02.-Building-&-Running).


**TODO**


We encourage contributions to the project. To contribute:

* Fork the project and create a new bug or feature branch.
* Make your commits with clean, understandable comments
* Perform a pull request


* [Lider Console](https://github.com/Pardus-Kurumsal/lider-console): Administration console built as Eclipse RCP project.
* [Ahenk](https://github.com/Pardus-Kurumsal/ahenk): Agent service running on remote machines.
* [Lider Ahenk Installer](https://github.com/Pardus-Kurumsal/lider-ahenk-installer): Installation wizard for Ahenk and Lider (and also its LDAP, database, XMPP servers).
* [Lider Ahenk Archetype](https://github.com/Pardus-Kurumsal/lider-ahenk-archetype): Maven archetype for easy plugin development.


Lider Ahenk and its sub projects are licensed under the [LGPL v3](https://github.com/Pardus-Kurumsal/lider/blob/master/LICENSE).