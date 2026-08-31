---
access_model:
  confidence: medium
  label: Self-serve signup
  onboarding: self-serve
  pricing: unknown
  public: false
  source:
  - authentication
  trial: false
  try_now: false
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
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.7
  scored_at: '2026-08-30'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Openfda Agentic Access
  operation_count: 22
  slug: openfda-agentic-access
  summary_line: 22 operations
api_count: 1
apis:
- description: Adverse events involving animal and veterinary products.
  name: openFDA Animal & Veterinary API
  slug: openfda-animal-veterinary-api
- description: Device-related endpoints (adverse events, classifications, recalls, 510(k), PMA, UDI).
  name: openFDA Device API
  slug: openfda-device-api
- description: Drug-related endpoints (adverse events, labeling, recalls, NDC).
  name: openFDA Drug API
  slug: openfda-drug-api
- description: Food-related endpoints (enforcement reports, adverse events).
  name: openFDA Food API
  slug: openfda-food-api
- description: Cross-cutting datasets (NSDE, substance, harmonized).
  name: openFDA Other API
  slug: openfda-other-api
- description: Tobacco product problem reports.
  name: openFDA Tobacco API
  slug: openfda-tobacco-api
artifact_total: 52
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: openFDA Animal & Veterinary API
  slug: open-openfda-animal-veterinary-api
- collection_type: open
  name: openFDA Animal & Veterinary Device API
  slug: open-openfda-device-api
- collection_type: open
  name: openFDA Animal & Veterinary Drug API
  slug: open-openfda-drug-api
- collection_type: open
  name: openFDA Animal & Veterinary Food API
  slug: open-openfda-food-api
- collection_type: open
  name: openFDA Animal & Veterinary Other API
  slug: open-openfda-other-api
- collection_type: open
  name: openFDA Animal & Veterinary Tobacco API
  slug: open-openfda-tobacco-api
- collection_type: open
  name: openFDA API
  slug: open-openfda
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/openfda-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/openfda-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/openfda-authentication.yml
- group: start
  title: ''
  type: Portal
  url: https://open.fda.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://open.fda.gov/apis/
- group: auth
  title: ''
  type: Authentication
  url: https://open.fda.gov/apis/authentication/
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
- group: docs
  title: ''
  type: Documentation
  url: https://open.fda.gov/apis/downloads/
- group: operate
  title: ''
  type: StatusPage
  url: https://open.fda.gov/about/status/
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
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/FDA/openfda
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/FDA/open.fda.gov
- group: docs
  title: ''
  type: Documentation
  url: https://www.fda.gov/
- group: operate
  title: ''
  type: Support
  url: https://www.fda.gov/about-fda/contact-fda
- group: commercial
  title: ''
  type: License
  url: https://creativecommons.org/publicdomain/zero/1.0/
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
  url: rules/openfda-rules.yml
- group: design
  title: ''
  type: SpectralRules
  url: rules/openfda-rules.yml
- group: design
  title: ''
  type: JSONLD
  url: json-ld/openfda-context.jsonld
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/openfda-vocabulary.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/openfda-rate-limits.yml
- group: docs
  title: ''
  type: JSONSchema
  url: json-schema/openfda-search-response-schema.json
- group: build
  title: ''
  type: Examples
  url: examples/openfda-drug-event-example.json
created: '2026-05-25'
description: openFDA is the U.S. Food and Drug Administration's public data platform, providing Elasticsearch-backed REST APIs serving FDA-administered data on drugs, medical devices, foods, animal and veterinary products, and tobacco. Twenty-two endpoints under a single api.fda.gov base URL expose adverse event reports (FAERS, MAUDE, CAERS), recall enforcement reports, Structured Product Labeling, the National Drug Code Directory, Drugs@FDA approvals, drug shortages, device classification, 510(k) and PMA submissions, Unique Device Identifier records, registration and listing, NSDE drug data, FDA substance harmonization, and historical FDA documents. All endpoints share a Lucene-style search, sort, count, limit, and skip parameter surface, are released under CC0 Public Domain, and operate under a free api.data.gov key that lifts daily quotas to 120,000 requests.
examples:
- key_count: 4
  name: Openfda Drug Event Example
  slug: openfda-drug-event-example
features:
- Six product-domain APIs (drug, device, food, animal & veterinary, tobacco, other) under a single api.fda.gov base URL
- Twenty-two Lucene-queryable JSON endpoints sharing search, sort, count, limit, and skip parameters
- Aggregation via the count parameter returns frequency histograms on any field without retrieving documents
- Bulk download of every dataset as JSON archives partitioned for resumable transfer
- Optional free api.data.gov API key lifts the per-IP daily quota from 1,000 to 120,000 requests
- Per-minute ceiling of 240 requests/min applies uniformly to anonymous and keyed callers
- Pagination capped at skip=25,000 with limit=1,000; deeper traversal requires bulk downloads
- All endpoints are CC0 Public Domain — no attribution required for commercial or research reuse
- Harmonized openfda block on most documents links each record back to NDC, UNII, SPL Set ID, and other identifiers
- HTTPS-only with HTTP Basic or query-parameter key authentication
- Public status page and email list for outage and breaking-change notifications
- Active developer community via the openFDA GitHub organization and community forum
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/openfda.png
integrations:
- description: Federal API gateway that issues and enforces the openFDA API key, applying rate limits and quotas.
  name: api.data.gov
- description: openFDA datasets are cataloged in the federal open-data portal as DCAT-compliant resources.
  name: data.gov
- description: NDC and Drugs@FDA records are commonly joined with NIH RxNorm to align brand, generic, and ingredient terminology.
  name: NIH RxNorm
- description: SPL drug labeling in openFDA mirrors NLM DailyMed, the authoritative SPL repository.
  name: NLM DailyMed
- description: openFDA device UDI records derive from FDA's Global Unique Device Identification Database.
  name: GUDID (Global UDI Database)
- description: openFDA drug adverse event endpoint surfaces the same FAERS data exposed in FDA's public dashboard.
  name: FAERS Public Dashboard
json_schemas:
- name: openFDA Search Response
  property_count: 2
  slug: openfda-search-response
jsonld:
- class_count: 17
  name: Openfda Context
  property_count: 5
  slug: openfda-context
layout: provider
modified: '2026-05-25'
name: openFDA
nav: Providers
network: true
overview: 'openFDA publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Animal & Veterinary API, Device API, Drug API, and 3 more. Tagged areas include Government, Healthcare, Drug, Device, and Food.


  The openFDA catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  openFDA''s developer surface includes authentication, developer portal, documentation, signup flow, getting-started guide, API reference, changelog, and 24 more developer resources.'
random_paper: 19
rate_limits:
- limit_count: 0
  name: Openfda Rate Limits
  slug: openfda-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: openFDA API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: openfda-jsonschema-spectral-rules
- effective_rule_count: 0
  extends: []
  name: openFDA API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: openfda-rules
score:
  band: developing
  composite: 50.6
  coverage:
    artifact_dirs: 12
    catalog_gap: 61.8
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: -0.5
  facets:
    access_clarity: 34.2
    commercial_clarity: 34.2
    contract_governance: 25.0
    contract_quality: 57.8
    developer_ergonomics: 54.8
    discoverability: 68.5
    governance: 25.0
    operational_transparency: 36.8
  previous_composite: 51.1
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 6
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 46.3
  schema_version: 0.17.2
  scored_at: '2026-08-30'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/openfda/refs/heads/main/screenshots/openfda-2026-06-20T190958.png
security:
- kind: authentication
  name: Openfda Authentication
  slug: openfda-authentication
  summary_line: apiKey · 1 scheme
- kind: domain-security
  name: Openfda Domain Security
  slug: openfda-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
slug: openfda
solutions:
- description: Continuously ingest drug, device, and food adverse events for safety signal detection.
  name: Pharmacovigilance
- description: Power weekly recall enforcement notification workflows across drug, device, and food domains.
  name: Recall and Withdrawal Alerting
- description: Aggregate 510(k), PMA, and Drugs@FDA submissions for competitive analysis and pipeline tracking.
  name: Regulatory Filings Intelligence
- description: Surface FDA labeling content as a reference layer (explicitly not for clinical decision-making per openFDA terms).
  name: Clinical Decision Support References
tags:
- Government
- Healthcare
- Drug
- Device
- Food
- Animal & Veterinary
- Tobacco
- Public Data
- Open Data
- Adverse Events
- Recalls
- Regulatory
use_cases:
- description: Mine FAERS, MAUDE, CAERS, and animal/veterinary adverse event reports for safety signals across drugs, devices, foods, and animal products.
  name: Adverse Event Surveillance
- description: Subscribe to drug, device, and food recall enforcement reports and surface them in clinical, retail, or supply-chain dashboards.
  name: Recall Monitoring
- description: Embed authoritative indications, dosage, warnings, and ingredient sections from Structured Product Labeling into consumer or clinical applications.
  name: Drug Labeling Apps
- description: Track 510(k) clearances, PMA approvals, and Drugs@FDA submissions to monitor competitor and pipeline activity.
  name: Regulatory Intelligence
- description: Look up NDC, UDI, UNII, and SPL Set IDs across product domains to power claims, EHR, and supply-chain integrations.
  name: Identifier Resolution
- description: Academic and journalistic investigation of adverse outcomes, recall patterns, and regulatory enforcement using CC0 public data.
  name: Public-Health Research
- description: Cross-reference drug shortage status, recall actions, and registration listings to detect upstream supply disruptions.
  name: Supply-Chain Risk
website: https://open.fda.gov/
---
