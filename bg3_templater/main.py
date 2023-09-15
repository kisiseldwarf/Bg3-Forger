import click
import os
import uuid
import chevron

template_dir = 'templates'

@click.group()
def cli():
    pass

def find(arr, el):
    try:
        return arr.index(el)
    except ValueError:
        return -1

@cli.command()
@click.argument("name")
@click.option("-l", "--lang", type = click.Choice(['en', 'fr'], case_sensitive=False), multiple=True, default = ["en"], help = "Languages to include in Localization")
def new(name, lang):
    os.mkdir(name)
    os.mkdir("{name}/Generated".format(name = name))
    os.mkdir("{name}/Public".format(name = name))
    os.mkdir("{name}/Public/{name}".format(name = name))
    os.mkdir("{name}/Localization".format(name = name))
    if (find(lang, 'en') != -1):
        os.mkdir("{name}/Localization/English".format(name = name))
    if (find(lang, 'fr') != -1):
        os.mkdir("{name}/Localization/French".format(name = name))
    os.mkdir("{name}/Mods".format(name = name))
    os.mkdir("{name}/Mods/{name}".format(name = name))


    with open('{template_dir}/meta.mustache'.format(template_dir = template_dir), 'r') as f:
        compiled_text = chevron.render(f, {
            "author_name": "kisis",
            "mod_description": "My super mod",
            "mod_folder": "???",
            "mod_name": name,
            "mod_id": uuid.uuid4()
        })
        targetFile = open("{name}/Mods/{name}/meta.lsx".format(name = name), "x")
        targetFile.write(compiled_text)
        targetFile.close()

    if(find(lang, 'en') != -1):
        open("{name}/Localization/English/{name}.xml".format(name = name), "x")
    if(find(lang, 'fr') != -1):
        open("{name}/Localization/French/{name}.xml".format(name = name), "x")
    open("{name}/Public/{name}/[PAK]_{name}".format(name = name), "x")

if __name__ == '__main__':
    cli()