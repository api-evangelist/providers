---
access_model:
  confidence: medium
  label: Free · Open access
  onboarding: open
  pricing: free
  public: true
  source:
  - plans
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 12.2
  scored_at: '2026-07-28'
api_count: 17
apis:
- description: Access FDA Adverse Event Reporting System (FAERS) data covering adverse event reports for drugs and therapeutic biologic products from 2004 onward, updated quarterly.
  name: Drug Adverse Events API
  slug: drug-adverse-events
- description: Access FDA Structured Product Labeling (SPL) files for prescription and over-the-counter drug products, including indications, adverse reactions, and safety information. Updated weekly.
  name: Drug Labeling API
  slug: drug-labeling
- description: Access drug product recall enforcement reports submitted to the FDA.
  name: Drug Recall Enforcement Reports API
  slug: drug-recall-enforcement
- description: Access 510(k) premarket notification data demonstrating that devices are at least as safe and effective as legally marketed predicate devices.
  name: Medical Device 510(k) Clearances API
  slug: device-510k
- description: Access reports of serious injuries, deaths, malfunctions, and other undesirable effects associated with the use of medical devices.
  name: Medical Device Adverse Event Reports API
  slug: device-adverse-events
- description: Access medical device names, product codes, specialty areas, and classification data.
  name: Medical Device Classification API
  slug: device-classification
- description: Access medical device product recall enforcement report data.
  name: Medical Device Recall Enforcement Reports API
  slug: device-recall-enforcement
- description: Access FDA scientific and regulatory review data for Class III medical devices requiring premarket approval.
  name: Medical Device Premarket Approval (PMA) API
  slug: device-pma
- description: Access actions taken to address problems with medical devices that violate FDA law.
  name: Medical Device Recalls API
  slug: device-recalls
- description: Access establishment locations and corresponding manufactured device listings.
  name: Medical Device Registrations and Listings API
  slug: device-registrations-listings
- description: Access Global Unique Device Identification Database (GUDID) information for medical devices.
  name: Unique Device Identifier (UDI) API
  slug: device-udi
- description: Access food product recall enforcement report data from the FDA.
  name: Food Recall Enforcement Reports API
  slug: food-recall-enforcement
- description: Access FDA CFSAN Adverse Event Reporting System (CAERS) data for food, dietary supplement, and cosmetic adverse event reports.
  name: Food Adverse Event Reports API (CAERS)
  slug: food-adverse-events
- description: Access reports about tobacco products that are damaged, defective, contaminated, or cause undesirable health effects.
  name: Tobacco Problem Reports API
  slug: tobacco-problem-reports
- description: Access tobacco prevention advertising and smokefree campaign research datasets examining advertising influence on youth attitudes and public health impact.
  name: Tobacco Research Datasets API
  slug: tobacco-research
- description: Access FDA press releases from 1913 to 2014 in searchable format.
  name: Historical FDA Documents API
  slug: other-historical-documents
- description: Access molecular-level substance information designed for internal and external applications, including the Unique Ingredient Identifier (UNII) listing.
  name: Substance Data API
  slug: other-substance-data
artifact_total: 41
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-fda-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://open.fda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://open.fda.gov/apis/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/FDA
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/FDA/openfda
- group: company
  title: ''
  type: Blog
  url: https://open.fda.gov/about/updates/
- group: operate
  title: ''
  type: StatusPage
  url: https://open.fda.gov/about/status/
- group: other
  title: ''
  type: X
  url: https://x.com/openFDA
- group: auth
  title: ''
  type: Authentication
  url: https://open.fda.gov/apis/authentication/
- group: commercial
  title: ''
  type: Plans
  url: plans/open-fda-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/open-fda-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/open-fda-finops.yml
created: '2026-06-13'
description: openFDA is the FDA's open data platform providing REST APIs for public access to FDA regulatory datasets. It covers drug adverse events (FAERS), drug labeling (SPL), drug recall enforcement reports, medical device 510(k) clearances, device adverse event reports, device recalls and classifications, food recall enforcement actions, food adverse events (CAERS), tobacco problem reports, tobacco research datasets, historical FDA documents, and substance data. All data is returned as JSON and is available free of charge with or without an API key.
examples:
- key_count: 2
  name: Device 510K
  slug: device-510k
- key_count: 2
  name: Device Adverse Event
  slug: device-adverse-event
- key_count: 2
  name: Device Classification
  slug: device-classification
- key_count: 2
  name: Drug Adverse Event
  slug: drug-adverse-event
- key_count: 2
  name: Drug Enforcement Recall
  slug: drug-enforcement-recall
- key_count: 2
  name: Drug Label
  slug: drug-label
- key_count: 2
  name: Food Adverse Event
  slug: food-adverse-event
- key_count: 2
  name: Food Enforcement Recall
  slug: food-enforcement-recall
- key_count: 2
  name: Substance Data
  slug: substance-data
- key_count: 2
  name: Tobacco Problem
  slug: tobacco-problem
finops:
- name: Open Fda Finops
  service_category: ''
  slug: open-fda-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-fda.png
json_schemas:
- name: Device 510K Clearance
  property_count: 24
  slug: device-510k-clearance
- name: Device Adverse Event
  property_count: 83
  slug: device-adverse-event
- name: Drug Adverse Event
  property_count: 27
  slug: drug-adverse-event
- name: Drug Label
  property_count: 179
  slug: drug-label
- name: Enforcement Recall
  property_count: 26
  slug: enforcement-recall
- name: Food Adverse Event
  property_count: 7
  slug: food-adverse-event
- name: Substance Data
  property_count: 21
  slug: substance-data
- name: Tobacco Problem
  property_count: 9
  slug: tobacco-problem
jsonld:
- class_count: 72
  name: Open Fda Context
  property_count: 11
  slug: open-fda-context
layout: provider
modified: '2026-06-13'
name: openFDA
nav: Providers
network: true
overview: 'openFDA publishes 17 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include FDA, Food and Drug Administration, Drug Safety, Adverse Events, and Drug Labels.


  The openFDA catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  openFDA''s developer surface includes documentation, engineering blog, authentication, and 9 more developer resources.'
plans:
- name: Open Fda Plans Pricing
  plan_count: 2
  slug: open-fda-plans-pricing
random_paper: 49
rate_limits:
- limit_count: 0
  name: Open Fda Rate Limits
  slug: open-fda-rate-limits
rules:
- name: openFDA API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: open-fda-jsonschema-spectral-rules
score:
  band: thin
  composite: 31.0
  delta: -5.1
  facets:
    commercial_clarity: 28.9
    contract_quality: 17.7
    developer_ergonomics: 21.7
    discoverability: 74.1
    governance: 52.1
    operational_transparency: 21.1
  previous_composite: 36.1
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 31.5
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/open-fda/refs/heads/main/screenshots/open-fda-2026-06-20T190739.png
security:
- kind: domain-security
  name: Open Fda Domain Security
  slug: open-fda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: open-fda
tags:
- FDA
- Food and Drug Administration
- Drug Safety
- Adverse Events
- Drug Labels
- Recalls
- Medical Devices
- Food Safety
- Tobacco
- Public Health
- Open Data
- Government
- Regulatory
- FAERS
- SPL
website: https://open.fda.gov/
---
