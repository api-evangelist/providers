---
aid: williams
name: Williams Companies
description: Williams Companies is a Fortune 500 energy infrastructure company that operates approximately 33,000 miles of natural gas pipeline infrastructure, moving roughly one-third of the nation's natural gas. The company's flagship Transco pipeline system spans 10,000 miles from south Texas to New York City and is the nation's largest-volume natural gas pipeline. Williams provides pipeline transportation, gathering, processing, and storage services across key natural gas supply basins and serves utilities, power generators, industrial customers, and local distribution companies across the United States.
type: Index
position: Producer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Energy
  - Natural Gas
  - Pipeline
  - Infrastructure
  - Fortune 500
  - Midstream
  - Utilities
created: '2026-05-03'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/williams/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: williams:transco-nominations
    name: Transco Nominations API
    description: The Transco Nominations API enables natural gas shippers to submit, modify, and track pipeline transportation nominations on the Transco pipeline system via the 1Line electronic bulletin board portal. Nominations define the quantity of gas a shipper wants to transport, the points of injection and withdrawal, and the scheduling period. The system supports online screen entry, flat file uploads, and EDI-based nomination submission.
    humanURL: https://www.1line.williams.com/Transco/index.html
    baseURL: https://www.1line.williams.com/Transco
    tags:
      - Energy
      - Natural Gas
      - Pipeline
      - Nominations
      - Transco
    properties:
      - type: Documentation
        url: https://www.1line.williams.com/Transco/index.html
      - type: Portal
        url: https://www.1line.williams.com/Transco/index.html
  - aid: williams:northwest-pipeline
    name: Northwest Pipeline EBB
    description: Northwest Pipeline is a major interstate natural gas pipeline operated by Williams, providing electronic bulletin board access for nominations and capacity management on the Northwest Pipeline system serving the Pacific Northwest and parts of the western United States.
    humanURL: https://www.1line.williams.com/NWP/index.html
    baseURL: https://www.1line.williams.com/NWP
    tags:
      - Energy
      - Natural Gas
      - Pipeline
      - Northwest
    properties:
      - type: Documentation
        url: https://www.1line.williams.com/NWP/index.html
      - type: Portal
        url: https://www.1line.williams.com/NWP/index.html
common:
  - type: Website
    url: https://www.williams.com
  - type: Portal
    url: https://www.williams.com
  - type: Documentation
    url: https://www.williams.com/pipeline/transco/
  - type: CustomerPortal
    url: https://www.1line.williams.com/Transco/index.html
  - type: ElectronicBulletinBoard
    url: https://www.williams.com/our-company/customer-electronic-bulletin-boards/
  - type: InvestorRelations
    url: https://investor.williams.com
  - type: Sustainability
    url: https://www.williams.com/sustainability/
  - type: PowerInnovation
    url: https://www.williams.com/power-innovation/
  - type: Operations
    url: https://www.williams.com/our-company/operations/
  - type: LinkedIn
    url: https://www.linkedin.com/company/williams-company
  - type: TermsOfService
    url: https://www.williams.com
  - type: JSONLDContext
    url: https://raw.githubusercontent.com/api-evangelist/williams/refs/heads/main/json-ld/williams-context.jsonld
  - type: Vocabulary
    url: https://raw.githubusercontent.com/api-evangelist/williams/refs/heads/main/vocabulary/williams-vocabulary.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
