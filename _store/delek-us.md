---
aid: delek-us
name: Delek US
description: 'Delek US is an alias for Delek US Holdings, Inc. (NYSE: DK), a diversified downstream energy company headquartered in Brentwood, Tennessee with assets in petroleum refining, logistics, asphalt operations, renewable fuels, and convenience store retailing. Delek operates four refineries in Tyler and Big Spring (Texas), El Dorado (Arkansas), and Krotz Springs (Louisiana) with combined crude throughput capacity of roughly 302,000 barrels per day. The canonical profile for this company is maintained under aid delek-us-holdings; this entry exists as a name alias and references the corporate site. Delek does not publish a developer API; partner integrations occur through industry-standard EDI, terminal automation, and ticketing systems.'
url: https://raw.githubusercontent.com/api-evangelist/delek-us/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: company
access: 3rd-Party
position: Consuming
tags:
  - Alias
  - Downstream
  - Energy
  - Petroleum
  - Refining
  - Retail
created: '2026-03-21'
modified: '2026-04-28'
apis:
  - aid: delek-us:delek-us-website
    name: Delek US Website
    description: Corporate website redirect for Delek US, the doing-business-as brand of Delek US Holdings, Inc. The canonical site is delekus.com and provides corporate, investor, and sustainability information.
    humanURL: https://www.delekus.com
    tags:
      - Corporate
      - Website
    properties:
      - type: Documentation
        url: https://www.delekus.com
common:
  - type: Website
    url: https://www.delekus.com
  - type: InvestorRelations
    url: https://ir.delekus.com
  - type: Alias
    url: https://raw.githubusercontent.com/api-evangelist/delek-us-holdings/refs/heads/main/apis.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
