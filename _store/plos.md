---
aid: plos
name: PLOS
description: These examples use the search API to search the PLOS corpus of scientific articles. These examples are not intended to be a full explanation on the use of Solr. A full Solr query language explanation can be found here and a tutorial here. The construction of PLOS search queries deviates from the standard Solr query URL by using search instead of select when making request to the end point. The primary endpoint is http://api.plos.org/search and supports parameters such as q, fl, wt, start, and rows for querying the PLOS Solr index.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Scientific Articles
  - Research
  - Search
  - Solr
  - Open Access
created: '2025-02-06'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/plos/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: plos:plos
    name: PLOS Search API
    description: These examples use the search API to search the PLOS corpus of scientific articles. These examples are not intended to be a full explanation on the use of Solr. A full Solr query language explanation can be found here and a tutorial here. The construction of PLOS search queries deviates from the standard Solr query URL by using search instead of select when making request to the end point.
    humanURL: https://api.plos.org/solr/examples/
    baseURL: http://api.plos.org/search
    tags:
      - Scientific Articles
      - Search
      - Solr
    properties:
      - type: Documentation
        url: https://api.plos.org/solr/examples/
      - type: SearchFields
        url: https://api.plos.org/solr/search-fields/
common:
  - type: Website
    url: https://plos.org
  - type: Documentation
    url: https://api.plos.org/solr/examples/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
