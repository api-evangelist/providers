---
aid: defense-security-cooperation-agency
name: Defense Security Cooperation Agency
description: The Defense Security Cooperation Agency (DSCA) is the U.S. Department of Defense agency that leads, directs, and manages security cooperation programs and resources to support U.S. policy and interests with foreign partners. DSCA administers the Foreign Military Sales (FMS) program, Foreign Military Financing (FMF) execution, International Military Education and Training (IMET), and humanitarian assistance programs. Public-facing surfaces include the Major Arms Sales notifications published in cooperation with Congress, the DSCA newsroom and library, and the Security Cooperation Workforce certification portal. DSCA does not publish a general-purpose developer API; partner-nation systems interact through controlled, government-to-government channels such as the Security Cooperation Information Portal (SCIP).
url: https://raw.githubusercontent.com/api-evangelist/defense-security-cooperation-agency/refs/heads/main/apis.yml
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
specificationVersion: '0.19'
xType: government
access: 3rd-Party
position: Consuming
tags:
  - Defense
  - Department of Defense
  - DSCA
  - Federal Government
  - Foreign Military Sales
  - International
  - Security Cooperation
created: '2024-12-03'
modified: '2026-04-28'
apis:
  - aid: defense-security-cooperation-agency:defense-security-cooperation-agency-website
    name: DSCA Website
    description: Public-facing website of the Defense Security Cooperation Agency that describes its mission, leadership, programs, and partners. The site links to news, the security cooperation library, and the FMS program but does not expose a developer API.
    humanURL: https://www.dsca.mil
    tags:
      - Federal Government
      - Website
    properties:
      - type: Documentation
        url: https://www.dsca.mil
  - aid: defense-security-cooperation-agency:defense-security-cooperation-agency-major-arms-sales
    name: DSCA Major Arms Sales Notifications
    description: DSCA publishes Major Arms Sales notifications and supporting transmittal documents that Congress and the public use to track potential Foreign Military Sales cases. Notifications are posted as web pages and PDFs without a documented API.
    humanURL: https://www.dsca.mil/press-media/major-arms-sales
    tags:
      - Arms Sales
      - FMS
      - Notifications
    properties:
      - type: Documentation
        url: https://www.dsca.mil/press-media/major-arms-sales
  - aid: defense-security-cooperation-agency:defense-security-cooperation-agency-scip
    name: Security Cooperation Information Portal (SCIP)
    description: Government-to-government portal that hosts case management, financial, and logistical information for security cooperation partners. SCIP requires authenticated access and operates outside the public developer ecosystem.
    humanURL: https://www.dsca.mil/policy/dsca-policy-systems/security-cooperation-information-portal-scip
    tags:
      - Case Management
      - Foreign Military Sales
      - Partner Nation
    properties:
      - type: Documentation
        url: https://www.dsca.mil/policy/dsca-policy-systems/security-cooperation-information-portal-scip
  - aid: defense-security-cooperation-agency:defense-security-cooperation-agency-workforce
    name: DSCA Security Cooperation Workforce Development
    description: DSCA portal supporting Security Cooperation Workforce certification, training, and the Defense Security Cooperation University (DSCU). Public information is available on the website with authenticated systems for enrolled professionals.
    humanURL: https://www.dscu.edu
    tags:
      - Certification
      - Training
      - Workforce
    properties:
      - type: Documentation
        url: https://www.dscu.edu
common:
  - type: Website
    url: https://www.dsca.mil
  - type: News
    url: https://www.dsca.mil/press-media/news-articles
  - type: Library
    url: https://www.dsca.mil/security-cooperation-library
  - type: ContactUs
    url: https://www.dsca.mil/contact
  - type: PrivacyPolicy
    url: https://www.dsca.mil/privacy-and-security-policy
  - type: FOIA
    url: https://open.defense.gov/Transparency/FOIA.aspx
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
