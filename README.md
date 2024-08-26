# Alfred Markdown Boookmarks

This workflow allows you to manage your bookmarks independent from your browser in a markdown file and access them quickly through alfred.

## Setup

1. Install the workflow
2. Set the location of your bookmarks file
3. Put your bookmarks into the markdown file
4. Have fun...

## File format
Bookmarks are stored as links in the markdown file - one link per row, i prefer to use bullet lists.
Headlines will be used to construct the title. This way you can organize your bookmarks in sections.

**Example:**

``` markdown
# Bookmarks
## Work
- [My Company](https://mycompany.com)
- [Duck Duck Go](https://duckduckgo.com)

## Hobbies
### Canoeing 
- [Lettmann Canoes](https://lettmann.com)
### Base Jumping
- [Base Jumping](https://iwoouldneverdothis.com)
```

This would end up in the following list in Alfred:

# Work/My company
# Work/Duck Duck go
# Hobbies/Canoeing/Lettmann Canoes
# Hobbies/Base Jumping/Base Jumping
