# geosites_site_template
To create a new site using geosites-project as a template. In the examples below site_name is a unique name for your site , example.org is the domain for the the site  ,the site_id is the unique id of the site and finally the project_name its the project of the geosites that you created.

    $ django-admin startproject site_name --template=https://github.com/thom03/geosites_site_template/archive/master.zip -epu,rst,yml

    $ cd site_name

    $ bash ./setup.sh example.org site_id project_name
