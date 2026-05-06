---
aid: election-assistance-commission
name: Election Assistance Commission
description: The U.S. Election Assistance Commission (EAC) was established by the Help America Vote Act of 2002 (HAVA). The EAC is an independent, bipartisan commission charged with developing guidance to meet HAVA requirements, adopting voluntary voting system guidelines, and serving as a national clearinghouse of information on election administration. The EAC also accredits testing laboratories, certifies voting systems, and audits the use of HAVA funds. The EAC publishes the Election Administration and Voting Survey (EAVS) datasets and operates an RSS news feed; it does not publish a formal developer API.
type: Contract
position: Consumer
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Federal Government
  - Elections
  - Voting
  - Open Data
created: '2024-12-03'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/election-assistance-commission/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: election-assistance-commission:eac
    name: Election Assistance Commission
    description: Public-facing presence of the U.S. Election Assistance Commission. The EAC publishes Election Administration and Voting Survey (EAVS) datasets, codebooks, voluntary voting system guidelines, voter list maintenance studies, and accessibility reports. Machine-readable access is currently limited to dataset downloads and an RSS news feed rather than a REST API.
    humanURL: https://www.eac.gov
    image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    tags:
      - Federal Government
      - Elections
      - Voting
      - Open Data
    properties:
      - type: Documentation
        url: https://www.eac.gov
      - type: ResearchAndData
        url: https://www.eac.gov/research-and-data
      - type: RSS
        url: https://www.eac.gov/rss.xml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - name: EAC Website
    url: https://www.eac.gov
    type: Website
  - name: EAC Research and Data
    url: https://www.eac.gov/research-and-data
    type: ResearchAndData
  - name: Election Administration and Voting Survey
    url: https://www.eac.gov/research-and-data/studies-and-reports
    type: Datasets
  - name: Voluntary Voting System Guidelines
    url: https://www.eac.gov/voting-equipment/voluntary-voting-system-guidelines
    type: Standards
  - name: EAC News RSS Feed
    url: https://www.eac.gov/rss.xml
    type: RSS
  - name: EAC Contact
    url: https://www.eac.gov/contact_us
    type: Contact
---
