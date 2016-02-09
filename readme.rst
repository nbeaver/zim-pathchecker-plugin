Bug report here: https://bugs.launchpad.net/zim/+bug/1419531

Relevant parts of the code:

- ``plugins/__init__.py``

  - ~/source-code-downloads/zim/zim-0.65/zim/plugins/__init__.py

    - "Short lived objects like individual pages, files, etc. will typically
      not be extended. To do something with them you need to extend the object
      that creates them."

- ``gui/pageview.py``

  - /usr/lib/python2.7/dist-packages/zim/gui/pageview.py
  - ~/source-code-downloads/zim/zim-0.65/zim/gui/pageview.py
  - especially:

   - ``InsertLinkDialog``
   - ``do_populate_popup``
   - ``_create_link_tag``

- Find the URLs:

  - use ``get_links()`` method from the ``Page`` class
    - uses ``get_parsetree().findall(zim.formats.LINK)``
    - does get a list of links, but no ability to change color of link.
  - use ``iter_get_zim_tags()`` method on something.
    - returns a list of ``gtk.TextTags``, so color can be modified (probably).
  - use on ``get_parsetree()`` directly
  - http://askubuntu.com/questions/272446/pygtk-textbuffer-adding-tags-and-reading-text

- Relevant signals:

  - 'link-clicked'
  - 'reload-page'

- Link coloring:

  - in ``pageview.py``, the ``tag_styles`` dict has ``'link': {'foreground': 'blue'},``
  - link are tags are ``gtk.TextTags``, so use ``tag.set_property('foreground', 'red')``

- Debugging.

  - Hard without stack traces.

    - http://stackoverflow.com/questions/916674/how-to-debug-pygtk-program
    - http://stackoverflow.com/questions/7726985/pygtk-console-output-for-debugging
