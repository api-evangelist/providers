---
aid: bureau-of-industry-security
url: https://raw.githubusercontent.com/api-evangelist/bureau-of-industry-security/refs/heads/main/apis.yml
name: Bureau of Industry Security
tags:
  - Compliance
  - Export Controls
  - Federal Government
  - Industries
  - National Security
  - Screening Lists
  - Security
type: Index
x-type: government
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2024-12-25'
modified: '2026-04-21'
position: Consumer
description: 'The Bureau of Industry and Security (BIS) is a division of the U.S. Department of Commerce that implements and enforces export control regulations to protect national security and prevent the proliferation of weapons of mass destruction. BIS reviews license applications for the export of sensitive goods and technologies, conducts outreach on compliance with export control laws, and maintains the Consolidated Screening List. Note: this entry is an alias for bureau-of-industry-and-security.'
apis:
  - aid: bureau-of-industry-security:consolidated-screening-list-api
    name: Consolidated Screening List (CSL) API
    tags:
      - Compliance
      - Export Controls
      - Federal Government
      - Sanctions
      - Screening
    humanURL: https://www.trade.gov/consolidated-screening-list
    baseURL: https://api.trade.gov/gateway/v1/consolidated_screening_list
    properties:
      - url: https://www.trade.gov/consolidated-screening-list
        type: Documentation
      - url: https://api.trade.gov/gateway/v1/consolidated_screening_list/search
        type: DataAPI
    description: The Consolidated Screening List (CSL) API consolidates export screening lists from the Departments of Commerce, State, and Treasury. It includes the Entity List, Denied Persons List, Unverified List (BIS), ITAR Debarred List (State), SDN List, and others. Used for trade compliance and due diligence screening.
    x-features:
      - Consolidated view of multiple export control screening lists
      - Full-text search by name, country, and address
      - Fuzzy name matching for due diligence
      - REST API with JSON responses
      - API key authentication via api.data.gov
    x-use-cases:
      - Export compliance screening before transactions
      - Automated trade partner due diligence
      - Sanctions and embargo verification
      - Regulatory compliance workflows
  - aid: bureau-of-industry-security:snap-r
    name: SNAP-R Export License Application System
    tags:
      - Export Controls
      - Federal Government
      - Licensing
    humanURL: https://snapr.bis.doc.gov/
    properties:
      - url: https://www.bis.gov/licensing/how-to-apply-snap-r
        type: Documentation
    description: SNAP-R (Simplified Network Application Process Redesign) is the BIS online system for applying for export licenses, classifications, and authorizations under the Export Administration Regulations (EAR).
common:
  - type: Website
    url: https://www.bis.gov
  - type: Privacy Policy
    url: https://www.bis.gov/privacy-policy
  - type: Consolidated Screening List
    url: https://www.trade.gov/consolidated-screening-list
  - type: Export Administration Regulations
    url: https://www.bis.gov/regulations/export-administration-regulations-ear
  - type: Commerce Control List
    url: https://www.bis.gov/regulations/commerce-control-list-ccl
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
specificationVersion: '0.19'
---
