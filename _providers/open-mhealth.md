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
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-08-26'
api_count: 0
artifact_total: 1
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-mhealth-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.openmhealth.org
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmhealth.org/documentation/
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmhealth.org/documentation/#/overview/get-started
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmhealth.org/documentation/#/schema-docs/schema-library
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmhealth.org/documentation/#/data-providers/about-shims
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmhealth.org/documentation/#/omh-on-fhir/omh-on-fhir-overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmhealth.org/documentation/#/healthkit/healthkit-overview
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmhealth.org/documentation/#/visualization-library/visualization-library-overview
- group: start
  title: ''
  type: SchemaRegistry
  url: https://w3id.org/openmhealth
- group: other
  title: ''
  type: Standards
  url: https://standards.ieee.org/ieee/1752/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openmhealth
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/schemas
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/shimmer
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/omh-dsu-ri
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/Granola
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/web-visualizations
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/OMH-on-FHIR
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/sample-data-generator
- group: build
  title: ''
  type: SourceCode
  url: https://github.com/openmhealth/registry.openmhealth.org
- group: operate
  title: ''
  type: Forums
  url: https://groups.google.com/d/forum/omh-developers
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/openmhealth
- group: operate
  title: ''
  type: Contact
  url: https://www.openmhealth.org/contact-us/
- group: commercial
  title: ''
  type: License
  url: https://www.apache.org/licenses/LICENSE-2.0
- group: company
  title: ''
  type: Blog
  url: https://www.openmhealth.org/feed/
created: '2026-05-25'
description: 'Open mHealth is a nonprofit, community-driven initiative that develops open standards and open-source software for making patient-generated health data interoperable across mobile apps, wearables, clinical systems, and electronic health records. Its core contribution is a library of clinically validated JSON Schema data point schemas — covering physical activity, sleep, heart rate, blood pressure, body weight, blood glucose, and other vital signs — with the sleep, physical-activity, and metadata schemas now superseded by IEEE 1752.1, the IEEE standard for Mobile Health Data co-shepherded by the Open mHealth community. Around the schemas Open mHealth ships a stack of Apache-2.0 reference implementations: Shimmer (a Java/Spring server that pulls health data from Fitbit, Google Fit, iHealth, Misfit, RunKeeper, and Withings APIs and normalizes it into Open mHealth or IEEE 1752.1 data points), omh-dsu-ri (a Data Storage Unit reference implementation exposing an OAuth 2.0-secured
  Data Point REST API on top of MongoDB and PostgreSQL), Granola (an Objective-C library that serializes Apple HealthKit samples into Open mHealth JSON), a web visualizations library built on D3 and Plottable.js, the OMH-on-FHIR mapping that aligns Open mHealth data points to HL7 FHIR resources, and a sample-data-generator. Open mHealth operates as the steward of the standard, the schema and unit registry at registry.openmhealth.org, and a developer community of thousands of developers and health organizations including Cornell Tech, Kaiser Permanente, Stanford School of Medicine, UC Davis, and UCSF. The project has no commercial API, no paid tier, and no hosted SaaS — all artifacts are open source under Apache 2.0 and the standard itself is openly published.'
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-mhealth.png
layout: provider
modified: '2026-05-25'
name: Open mHealth
nav: Providers
network: true
overview: 'Open mHealth is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Health, Healthcare, Mobile Health, mHealth, and Digital Health.


  Open mHealth''s developer surface includes documentation, engineering blog, and 23 more developer resources.'
random_paper: 0
score:
  band: minimal
  composite: 6.0
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 6.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 7.5
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-mhealth/refs/heads/main/screenshots/open-mhealth-2026-06-20T190842.png
security:
- kind: domain-security
  name: Open Mhealth Domain Security
  slug: open-mhealth-domain-security
  summary_line: TLSv1.3
slug: open-mhealth
tags:
- Health
- Healthcare
- Mobile Health
- mHealth
- Digital Health
- Health Data
- Patient Generated Health Data
- Wearables
- Fitness
- Interoperability
- Open Standards
- Open-Source
- JSON-Schema
- IEEE 1752
- FHIR
- HealthKit
- Non-Profit
website: https://www.openmhealth.org
---
