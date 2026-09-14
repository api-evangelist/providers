---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source:
  - '{''url'': ''https://www.vera.com'', ''status'': 301, ''note'': ''declared website redirects to https://www.fortra.com/platform/secure-collaboration — a different registrable domain (vera.com -> fortra.com), possible rename or acquisition (probed 2026-09-03, roadmap#169)''}'
  trial: false
  try_now: false
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/vera-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.vera.com
- group: other
  title: ''
  type: ProductPage
  url: https://www.fortra.com/platform/secure-collaboration
- group: operate
  title: ''
  type: ChangeLog
  url: https://hstechdocs.helpsystems.com/releasenotes/Content/_ProductPages/Vera/VeraReleaseNotes_MainPage.htm
- group: operate
  title: ''
  type: ChangeLog
  url: changelog/vera-changelog.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/vera-llms.txt
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/vera-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.fortra.com/security/policy
- group: auth
  title: ''
  type: TrustCenter
  url: security/vera-trust-center.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.fortra.com/security
created: '2026-07-17'
description: Vera was a data-centric security company delivering information rights management (IRM) as a service, letting businesses encrypt, track, audit, and revoke access to files anywhere they travel, with an SDK and REST API for embedding AES 256-bit encryption and policy enforcement into applications. Backed by Amplify Partners, Battery Ventures, and Sutter Hill Ventures, Vera was acquired by HelpSystems (now Fortra) in December 2020 and lives on as Fortra's Digital Guardian Secure Collaboration product; its developer surface (SDK/REST API) is now available to Fortra customers rather than as a public developer program.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/vera.png
layout: provider
modified: '2026-07-21'
name: Vera
nav: Providers
network: true
overview: 'Vera is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Cybersecurity, Data Security, Encryption, and Digital Rights Management.


  Vera''s developer surface includes changelog and 9 more developer resources.'
random_paper: 10
screenshot: https://raw.githubusercontent.com/api-evangelist/vera/refs/heads/main/screenshots/vera-2026-09-02T165701.png
security:
- kind: domain-security
  name: Vera Domain Security
  slug: vera-domain-security
  summary_line: TLSv1.2 · DMARC
- kind: vulnerability-disclosure
  name: Vera Vulnerability Disclosure
  slug: vera-vulnerability-disclosure
  summary_line: disclosure policy published
- kind: trust-center
  name: Vera Trust Center
  slug: vera-trust-center
  summary_line: SOC 2 Type 2 (Digital Guardian product line, attested by Schellman & Company)
slug: vera
tags:
- Company
- Cybersecurity
- Data Security
- Encryption
- Digital Rights Management
- Information Rights Management
- Secure Collaboration
website: https://www.vera.com
---
