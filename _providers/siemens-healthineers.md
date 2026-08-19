---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
  trial: false
  try_now: false
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-19'
api_count: 14
apis:
- description: Authentication and identity federation surface that lets partner applications running on the teamplay digital health platform, syngo.via OpenApps, and Cios mobile C-arm systems sign users in using the
  name: teamplay Single Sign-On API
  slug: teamplay-single-sign-on-api
- description: Licensing management surface used by partner applications to validate, provision, and reconcile subscription entitlements within the teamplay Cloud Platform and syngo.via OpenApps environments. Listed
  name: teamplay Licensing API
  slug: teamplay-licensing-api
- description: User management surface that exposes user roles and permission assignments to partner applications on the teamplay digital health platform. Allows partner solutions to align in-application access cont
  name: teamplay User Roles and Permissions API
  slug: teamplay-user-roles-permissions-api
- description: 'Plug-in surface for the teamplay receiver, the on-premises agent that collects operational and clinical telemetry from imaging devices and transmits it to the teamplay Cloud Platform. Used by partner '
  name: teamplay Receiver Plug-in API
  slug: teamplay-receiver-plugin-api
- description: Imaging access surface enabling partner applications to retrieve DICOM studies and instances stored in the teamplay digital health platform. Supports the secure peer sharing and processing use cases h
  name: teamplay DICOM Image Access API
  slug: teamplay-dicom-image-access-api
- description: 'Submission surface allowing partner applications to push customer-specific reports and clinical results back into the teamplay digital health platform so they are accessible alongside native teamplay '
  name: teamplay Reports and Results Submission API
  slug: teamplay-reports-results-api
- description: Notification surface that lets partner applications publish status indicators (operational state, health, processing progress) into the teamplay digital health platform so customers see partner applic
  name: teamplay Status Indicator Notifications API
  slug: teamplay-status-notifications-api
- description: Research-oriented SDK that lets clinicians, researchers, and developers turn research ideas into deployable image-post-processing applications inside syngo.via. Frontier applications are distributed t
  name: syngo.via Frontier Development Kit
  slug: syngovia-frontier-development-kit
- description: Application platform inside syngo.via that hosts third-party and Siemens Healthineers research and clinical apps distributed through the Digital Marketplace. Partner apps integrate with syngo.via Open
  name: syngo.via OpenApps Platform
  slug: syngovia-openapps-platform
- description: 'Curated catalog distributing Siemens Healthineers and partner clinical and operational applications across the teamplay digital health platform, syngo.via OpenApps, and Cios mobile C-arm systems. All '
  name: Siemens Healthineers Digital Marketplace
  slug: digital-marketplace
- description: Open-source Kubernetes distribution built specifically for Windows hosts, published from the Siemens-Healthineers GitHub org. Provides cluster lifecycle tooling (install, upgrade, observe) for running
  name: K2s Kubernetes Distribution for Windows Hosts
  slug: k2s-kubernetes-distribution
- description: PHP-based platform from the Siemens-Healthineers GitHub org focused on medical device cybersecurity and US FDA compliance workflows. Provides automation for the documentation and lifecycle obligations
  name: SHIELD-DAVE Medical Device Cybersecurity Platform
  slug: shield-dave
- description: 'C# command-line tool published by Siemens Healthineers for analyzing Event Tracing for Windows (ETW) capture files using a query syntax. Used in performance and diagnostics workflows on Windows-based '
  name: ETWAnalyzer Command Line Tool
  slug: etwanalyzer
- description: 'Python research project from the Siemens-Healthineers GitHub org that extends the CLIP architecture with patch-level embeddings for image understanding. Relevant to medical imaging research pipelines '
  name: Patch-CLIP Embedding Model
  slug: patch-clip
artifact_total: 17
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/siemens-healthineers-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/siemens-healthineers-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.siemens-healthineers.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://devportal.us.api.teamplay.siemens-healthineers.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.frontier.api.teamplay.siemens-healthineers.com/
- group: start
  title: ''
  type: Signup
  url: https://devportal.us.api.teamplay.siemens-healthineers.com/signup
- group: start
  title: ''
  type: Login
  url: https://devportal.us.api.teamplay.siemens-healthineers.com/signin
- group: other
  title: ''
  type: Marketplace
  url: https://marketplace.teamplay.siemens.com/
- group: company
  title: ''
  type: PartnerProgram
  url: https://www.siemens-healthineers.com/en-us/digital-health-solutions/digital-marketplace-for-partners
- group: other
  title: ''
  type: DigitalHealthPlatform
  url: https://www.siemens-healthineers.com/digital-health-solutions/digital-solutions-overview/service-line-managment-solutions/teamplay
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Siemens-Healthineers
- group: company
  title: ''
  type: Press
  url: https://www.siemens-healthineers.com/press
- group: company
  title: ''
  type: Investors
  url: https://www.siemens-healthineers.com/investor-relations
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/siemens-healthineers-vocabulary.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/siemens-healthineers-context.jsonld
created: '2026-05-23'
description: Siemens Healthineers AG is a German medical technology company (XETRA SHL) covering medical imaging, laboratory diagnostics, point-of-care testing, advanced therapies, and cancer care (following the April 2021 Varian Medical Systems acquisition for USD 16.4 billion). Its digital surface is anchored by the teamplay digital health platform, the Digital Marketplace, syngo.via OpenApps, and the Frontier Development Kit, with developer access offered through a gated teamplay developer portal that exposes APIs for single sign-on, licensing, user roles and permissions, the teamplay receiver plug-in, DICOM image access, customer-specific report submission, and status indicator notifications. No public OpenAPI specifications are published; the API catalog and reference documentation sit behind teamplay developer account authentication.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/siemens-healthineers.png
jsonld:
- class_count: 58
  name: Siemens Healthineers Context
  property_count: 2
  slug: siemens-healthineers-context
layout: provider
modified: '2026-05-23'
name: Siemens Healthineers
nav: Providers
network: true
overview: 'Siemens Healthineers publishes 14 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Healthcare, Medical Imaging, Laboratory Diagnostics, Cancer Care, and Radiation Oncology.


  The Siemens Healthineers catalog on APIs.io includes 1 JSON-LD context.


  Siemens Healthineers'' developer surface includes signup flow, GitHub presence, and 13 more developer resources.'
random_paper: 140
score:
  band: emerging
  composite: 13.5
  delta: -3.3
  facets:
    access_clarity: 6.6
    commercial_clarity: 6.6
    contract_governance: 15.2
    contract_quality: 11.3
    developer_ergonomics: 0.0
    discoverability: 64.8
    governance: 15.2
    operational_transparency: 5.3
  previous_composite: 16.8
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/siemens-healthineers/refs/heads/main/screenshots/siemens-healthineers-2026-06-20T193903.png
security:
- kind: domain-security
  name: Siemens Healthineers Domain Security
  slug: siemens-healthineers-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Siemens Healthineers Vulnerability Disclosure
  slug: siemens-healthineers-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: siemens-healthineers
tags:
- Healthcare
- Medical Imaging
- Laboratory Diagnostics
- Cancer Care
- Radiation Oncology
- DICOM
- Digital Health
- Healthcare IT
- Medical Devices
- Teamplay
website: https://www.siemens-healthineers.com/
---
