
Relevant parts of the code:

- pageview.py
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
