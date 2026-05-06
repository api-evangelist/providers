---
aid: defense-threat-reduction-agency
name: Defense Threat Reduction Agency
description: The Defense Threat Reduction Agency (DTRA) is the U.S. Department of Defense combat support agency that counters and deters weapons of mass destruction (WMD) and improvised threats. DTRA leads the chemical, biological, radiological, nuclear, and high-yield explosive (CBRNE) mission for DoD and supports the Cooperative Threat Reduction (CTR) Program with partner nations. Public-facing surfaces include the DTRA website, the DTRA Information Analysis Center (DTRIAC) for technical reports, the DTRA Mission Network public information, and small-business and broad-agency-announcement procurement portals. DTRA does not publish a general-purpose developer API; partner systems interact through controlled, government-to-government channels.
url: https://raw.githubusercontent.com/api-evangelist/defense-threat-reduction-agency/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: government
access: 3rd-Party
position: Consuming
tags:
  - CBRNE
  - Counter-WMD
  - Defense
  - Department of Defense
  - DTRA
  - Federal Government
  - National Security
  - Threat Reduction
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: defense-threat-reduction-agency:defense-threat-reduction-agency-website
    name: DTRA Website
    description: Public-facing website of the Defense Threat Reduction Agency providing organizational information, leadership, news, and links to mission-area programs. The site does not expose a developer API.
    humanURL: https://www.dtra.mil
    tags:
      - Federal Government
      - Website
    properties:
      - type: Documentation
        url: https://www.dtra.mil
  - aid: defense-threat-reduction-agency:defense-threat-reduction-agency-dtriac
    name: DTRA Information Analysis Center (DTRIAC)
    description: The DTRA Information Analysis Center provides scientific and technical information services to the Counter-WMD community, including a managed library of technical reports and analysis products. Public discovery is limited and access requires registration.
    humanURL: https://www.dtra.mil/Mission/Cooperative-Threat-Reduction
    tags:
      - Library
      - Reports
      - Scientific and Technical Information
    properties:
      - type: Documentation
        url: https://www.dtra.mil/Mission/Cooperative-Threat-Reduction
  - aid: defense-threat-reduction-agency:defense-threat-reduction-agency-business
    name: DTRA Doing Business
    description: Procurement and partnership portal that publishes solicitations, Broad Agency Announcements, small-business opportunities, and points of contact for working with DTRA.
    humanURL: https://www.dtra.mil/Doing-Business-With-DTRA
    tags:
      - Acquisition
      - Contracting
      - Procurement
      - Small Business
    properties:
      - type: Documentation
        url: https://www.dtra.mil/Doing-Business-With-DTRA
  - aid: defense-threat-reduction-agency:defense-threat-reduction-agency-foia
    name: DTRA FOIA Reading Room
    description: Online portal that publishes records released under the Freedom of Information Act and frequently requested documents.
    humanURL: https://www.dtra.mil/FOIA
    tags:
      - FOIA
      - Open Records
      - Transparency
    properties:
      - type: Documentation
        url: https://www.dtra.mil/FOIA
common:
  - type: Website
    url: https://www.dtra.mil
  - type: News
    url: https://www.dtra.mil/News
  - type: ContactUs
    url: https://www.dtra.mil/Contact-Us
  - type: PrivacyPolicy
    url: https://www.dtra.mil/Privacy-and-Security
  - type: FOIA
    url: https://www.dtra.mil/FOIA
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
