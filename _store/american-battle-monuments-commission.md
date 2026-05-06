---
aid: american-battle-monuments-commission
name: American Battle Monuments Commission
description: The American Battle Monuments Commission (ABMC), established by Congress in 1923, commemorates the service, achievements, and sacrifice of U.S. Armed Forces. ABMC administers and maintains 26 American military cemeteries and 31 memorials, monuments, and markers on foreign soil. The commission maintains a searchable database of more than 200,000 fallen service members buried or commemorated abroad, accessible via the We Remember burial search portal. ABMC is working on a data roadmap to provide open datasets on data.gov per the Foundations for Evidence-based Policymaking Act (2019).
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Military
  - Veterans
  - World War II
  - Memorial
  - Open Data
url: https://raw.githubusercontent.com/api-evangelist/american-battle-monuments-commission/refs/heads/main/apis.yml
access: 3rd-Party
created: '2024-11-21'
modified: '2026-04-19'
position: Consumer
specificationVersion: '0.19'
apis:
  - aid: american-battle-monuments-commission:we-remember
    name: ABMC We Remember Burial Search
    description: The ABMC We Remember portal provides a searchable database of more than 200,000 fallen U.S. service members buried or commemorated at American military cemeteries abroad. Includes World War II Registry and Korean War Honor Roll records. Searches can be performed by last name and other criteria across ABMC cemeteries and memorials worldwide.
    humanURL: https://weremember.abmc.gov/
    baseURL: https://weremember.abmc.gov
    tags:
      - Veterans
      - Military Burials
      - World War II
      - Korean War
      - Memorial
    properties:
      - type: Documentation
        url: https://www.abmc.gov/about-us/reports-policy/data/
      - type: Portal
        url: https://weremember.abmc.gov/
common:
  - type: Website
    url: https://www.abmc.gov/
  - type: Portal
    url: https://weremember.abmc.gov/
  - type: Features
    data:
      - name: Burial Search Database
        description: Searchable database of more than 200,000 fallen service members buried or commemorated at ABMC cemeteries and memorials abroad, searchable by name and cemetery.
      - name: World War II Registry
        description: Database of U.S. servicemembers who lost their lives during World War II, accessible via the ABMC WWII Registry portal.
      - name: Korean War Honor Roll
        description: Registry of U.S. servicemembers who gave their lives during the Korean War, searchable through the We Remember portal.
      - name: Cemetery and Memorial Information
        description: Information about 26 American military cemeteries and 31 memorials, monuments, and markers on foreign soil including virtual 360-degree tours.
      - name: Open Data Roadmap
        description: ABMC is developing a data roadmap to provide access to datasets hosted on data.gov per the Foundations for Evidence-based Policymaking Act (2019), with a designated Chief Data Officer.
  - type: UseCases
    data:
      - name: Family Research
        description: Families and descendants search for fallen service members buried at ABMC cemeteries to locate burial information and plan visits.
      - name: Historical Research
        description: Historians, researchers, and educators access burial and memorial records for World War II, Korean War, and other conflicts.
      - name: Memorial Planning
        description: ABMC administrators and partner organizations use cemetery and memorial data for ceremony planning and site maintenance.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
