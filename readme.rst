
Relevant parts of the code:

- ``__init__.py``

  - ~/source-code-downloads/zim/zim-0.65/zim/plugins/__init__.py

    - "Short lived objects like individual pages, files, etc. will typically
      not be extended. To do something with them you need to extend the object
      that creates them."

- ``pageview.py``

  - /usr/lib/python2.7/dist-packages/zim/gui/pageview.py
  - ~/source-code-downloads/zim/zim-0.65/zim/gui/pageview.py
  - especially:

   - ``InsertLinkDialog``
   - ``do_populate_popup``
   - ``_create_link_tag``

- Find the URLs:

  - Iterate over all TextTags in buffer?
  - ``for element in node.getchildren():``

- Relevant signals:

  - 'link-clicked'
  - 'reload-page'

- Link coloring:

  - ``'link': {'foreground': 'blue'},``
