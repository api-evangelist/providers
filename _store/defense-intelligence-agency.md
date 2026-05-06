---
aid: defense-intelligence-agency
name: Defense Intelligence Agency
description: The Defense Intelligence Agency (DIA) is the U.S. Department of Defense combat support agency that produces, analyzes, and disseminates military intelligence on foreign militaries and operating environments to support warfighters, defense planners, and national-security policymakers. As an intelligence agency, DIA does not publish a general-purpose public API; its developer-facing surface is largely internal or restricted to the Intelligence Community. Public touchpoints include the GAMECHANGER policy analytics initiative, the DIA FOIA reading room, public news and article feeds, and procurement and recruiting portals.
url: https://raw.githubusercontent.com/api-evangelist/defense-intelligence-agency/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: government
access: 3rd-Party
position: Consuming
tags:
  - Defense
  - Department of Defense
  - DIA
  - Federal Government
  - Intelligence
  - Military Intelligence
  - National Security
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: defense-intelligence-agency:defense-intelligence-agency-website
    name: Defense Intelligence Agency Website
    description: Public-facing presence of the Defense Intelligence Agency, providing organizational information, leadership, careers, news, and links to mission-specific programs. The website is the primary public surface for DIA but does not expose a general-purpose developer API.
    humanURL: https://www.dia.mil
    tags:
      - Federal Government
      - Intelligence
      - Website
    properties:
      - type: Documentation
        url: https://www.dia.mil
      - type: News
        url: https://www.dia.mil/News
  - aid: defense-intelligence-agency:defense-intelligence-agency-foia
    name: Defense Intelligence Agency FOIA Reading Room
    description: Online portal that publishes records released under the Freedom of Information Act, including frequently requested documents and declassified materials. Researchers can browse and download released records but there is no documented public API.
    humanURL: https://www.dia.mil/FOIA
    tags:
      - FOIA
      - Open Records
      - Transparency
    properties:
      - type: Documentation
        url: https://www.dia.mil/FOIA
  - aid: defense-intelligence-agency:defense-intelligence-agency-gamechanger
    name: Defense Intelligence Agency GAMECHANGER
    description: A policy analytics platform led by DIA in partnership with the Office of the Undersecretary of Defense for Intelligence and Security that ingests, normalizes, and searches tens of thousands of DoD policy documents. GAMECHANGER is referenced in DIA public articles but does not publish a public developer API.
    humanURL: https://www.dia.mil/News-Features/Articles/Article-View/Article/2926343/gamechanger
    tags:
      - Analytics
      - Policy
      - Search
    properties:
      - type: Documentation
        url: https://www.dia.mil/News-Features/Articles/Article-View/Article/2926343/gamechanger
common:
  - type: Website
    url: https://www.dia.mil
  - type: Careers
    url: https://www.dia.mil/Careers
  - type: News
    url: https://www.dia.mil/News
  - type: FOIA
    url: https://www.dia.mil/FOIA
  - type: ContactUs
    url: https://www.dia.mil/Contact
  - type: PrivacyPolicy
    url: https://www.dia.mil/Privacy
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
