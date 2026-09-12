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
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 11.0
  scored_at: '2026-09-12'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Open Fda Agentic Access
  operation_count: 22
  slug: open-fda-agentic-access
  summary_line: 22 operations
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
artifact_total: 45
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/open-fda-agentic-access.yml
- group: start
  title: ''
  type: Portal
  url: https://open.fda.gov/
- group: start
  title: ''
  type: Signup
  url: https://api.data.gov/signup/
- group: start
  title: ''
  type: GettingStarted
  url: https://open.fda.gov/apis/try-the-api/
- group: docs
  title: ''
  type: APIReference
  url: https://open.fda.gov/apis/query-parameters/
- group: docs
  title: ''
  type: APIReference
  url: https://open.fda.gov/apis/query-syntax/
- group: docs
  title: ''
  type: APIReference
  url: https://open.fda.gov/apis/advanced-syntax/
- group: design
  title: ''
  type: ErrorCodes
  url: https://open.fda.gov/apis/errors/
- group: operate
  title: ''
  type: ChangeLog
  url: https://open.fda.gov/updates/
- group: operate
  title: ''
  type: Forums
  url: https://open.fda.gov/community/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FDA
- group: operate
  title: ''
  type: Support
  url: https://www.fda.gov/about-fda/contact-fda
- group: commercial
  title: ''
  type: TermsOfService
  url: https://open.fda.gov/terms/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.fda.gov/about-website/website-policies
- group: design
  title: ''
  type: Rules
  url: rules/open-fda-rules.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/open-fda-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/open-fda-vocabulary.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/open-fda-search-response-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/open-fda-drug-event-example.json
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/FDA/openfda/issues
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/FDA/openfda/blob/master/SECURITY.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/FDA/openfda/blob/master/CONTRIBUTING.txt
- group: commercial
  title: ''
  type: License
  url: https://github.com/FDA/openfda/blob/master/LICENSE
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
- key_count: 4
  name: Open Fda Drug Event Example
  slug: open-fda-drug-event-example
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
- name: openFDA Search Response
  property_count: 2
  slug: open-fda-search-response
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


  The openFDA catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  openFDA''s developer surface includes developer portal, signup flow, getting-started guide, API reference, changelog, support, code examples, and 28 more developer resources.'
plans:
- name: Open Fda Plans Pricing
  plan_count: 2
  slug: open-fda-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 0
  name: Open Fda Rate Limits
  slug: open-fda-rate-limits
rules:
- effective_rule_count: 2
  extends: []
  name: openFDA API Rules
  rule_count: 2
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 2
  slug: open-fda-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: openFDA API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: open-fda-rules
score:
  band: developing
  composite: 45.8
  coverage:
    artifact_dirs: 12
    catalog_earned: 69.5
    catalog_earned_first_party: 0.0
    catalog_gap: 45.5
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 52.6
    contract_governance: 22.7
    contract_quality: 21.3
    developer_ergonomics: 57.1
    discoverability: 74.1
    operational_transparency: 44.7
  previous_composite: 45.8
  provenance:
    agentic_access: derived
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 38.9
  schema_version: 0.21.0
  scored_at: '2026-09-12'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
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
