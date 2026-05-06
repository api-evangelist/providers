---
aid: internet-engineering-task-force
name: Internet Engineering Task Force
description: The Internet Engineering Task Force (IETF) is an open, global community of network designers, engineers, researchers, and operators that develops and promotes voluntary technical standards to ensure the smooth operation and evolution of the internet. The IETF publishes freely accessible RFCs (Requests for Comments) that serve as the foundation for internet interoperability. The IETF Datatracker exposes a public read-only REST API over the working group, document, and meeting data managed by the IETF.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Internet
  - Protocols
  - RFC
  - Standards
  - Working Groups
url: https://raw.githubusercontent.com/api-evangelist/internet-engineering-task-force/refs/heads/main/apis.yml
created: '2025-08-25'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: internet-engineering-task-force:ietf-datatracker-api
    name: IETF Datatracker API
    description: The IETF Datatracker REST API provides programmatic, read-only access to IETF data including documents, RFCs, drafts, working groups, meetings, IPR disclosures, and IESG ballot positions. Responses are returned as JSON or XML. Public endpoints require no authentication.
    humanURL: https://datatracker.ietf.org/api/
    baseURL: https://datatracker.ietf.org/api/v1/
    tags:
      - Internet
      - RFC
      - Standards
      - Working Groups
    properties:
      - type: Documentation
        url: https://datatracker.ietf.org/api/
      - type: SignUp
        url: https://datatracker.ietf.org/accounts/login/
  - aid: internet-engineering-task-force:rfc-editor
    name: RFC Editor
    description: The RFC Editor publishes the canonical RFC series in multiple formats (TXT, HTML, PDF, XML) and provides bulk and machine-readable indexes of RFCs and Internet-Drafts.
    humanURL: https://www.rfc-editor.org/
    baseURL: https://www.rfc-editor.org/
    tags:
      - RFC
      - Standards
    properties:
      - type: Documentation
        url: https://www.rfc-editor.org/retrieve/
      - type: Bulk
        url: https://www.rfc-editor.org/in-notes/rfc-index.xml
common:
  - type: Website
    url: https://www.ietf.org/
  - type: GitHub Organization
    url: https://github.com/ietf/
  - type: Datatracker
    url: https://datatracker.ietf.org/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
