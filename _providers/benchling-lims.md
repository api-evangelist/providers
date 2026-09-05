---
access_model:
  confidence: high
  label: Freemium · Self-serve signup
  onboarding: self-serve
  pricing: freemium
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: true
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: negotiable
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 27.0
  scored_at: '2026-09-04'
agentic_access:
- acting_count: 47
  human_in_the_loop: 0
  name: Benchling Lims Agentic Access
  operation_count: 89
  slug: benchling-lims-agentic-access
  summary_line: 89 operations · 47 acting
api_count: 1
apis:
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Amino-acid (protein) sequences.
  name: Benchling AA Sequences API
  slug: benchling-lims-aa-sequences-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Benchling Apps, app config, canvases, and sessions.
  name: Benchling Apps API
  slug: benchling-lims-apps-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Structured assay results, including transactional bulk loads.
  name: Benchling Assay Results API
  slug: benchling-lims-assay-results-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Assay runs and their automation input/output generators.
  name: Benchling Assay Runs API
  slug: benchling-lims-assay-runs-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Binary attachments and file objects.
  name: Benchling Blobs & Files API
  slug: benchling-lims-blobs-files-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Schema-driven custom entities registered in Benchling.
  name: Benchling Custom Entities API
  slug: benchling-lims-custom-entities-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: DNA sequences and sequence-aware operations.
  name: Benchling DNA Sequences API
  slug: benchling-lims-dna-sequences-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Electronic lab notebook (ELN) entries and templates.
  name: Benchling Entries API
  slug: benchling-lims-entries-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Tenant event stream (also delivered via EventBridge and webhooks).
  name: Benchling Events API
  slug: benchling-lims-events-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Locations, boxes, containers, and plates for physical samples.
  name: Benchling Inventory API
  slug: benchling-lims-inventory-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Automation input generators and output processors for instrument files.
  name: Benchling Lab Automation API
  slug: benchling-lims-lab-automation-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Small molecules.
  name: Benchling Molecules API
  slug: benchling-lims-molecules-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: DNA/RNA oligos.
  name: Benchling Oligos API
  slug: benchling-lims-oligos-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Organize entries and entities into projects and folders.
  name: Benchling Projects & Folders API
  slug: benchling-lims-projects-folders-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Register/unregister entities and browse registry schemas and dropdowns.
  name: Benchling Registry API
  slug: benchling-lims-registry-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Cross-team service requests, tasks, and fulfillments.
  name: Benchling Requests API
  slug: benchling-lims-requests-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: RNA sequences and sequence-aware operations.
  name: Benchling RNA Sequences API
  slug: benchling-lims-rna-sequences-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The Teams & Organizations API from Benchling — 4 operation(s) for teams & organizations.
  name: Benchling Teams & Organizations API
  slug: benchling-lims-teams-organizations-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: The Users API from Benchling — 4 operation(s) for users.
  name: Benchling Users API
  slug: benchling-lims-users-api
- baseURL: https://{tenant}.benchling.com/api/v2
  baseurl_source: declared
  description: Workflow task groups, tasks, and outputs.
  name: Benchling Workflows API
  slug: benchling-lims-workflows-api
artifact_total: 50
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Benchling AA Sequences API
  slug: open-benchling-lims-aa-sequences-api
- collection_type: open
  name: Benchling AA Sequences Apps API
  slug: open-benchling-lims-apps-api
- collection_type: open
  name: Benchling AA Sequences Assay Results API
  slug: open-benchling-lims-assay-results-api
- collection_type: open
  name: Benchling AA Sequences Assay Runs API
  slug: open-benchling-lims-assay-runs-api
- collection_type: open
  name: Benchling AA Sequences Blobs & Files API
  slug: open-benchling-lims-blobs-files-api
- collection_type: open
  name: Benchling AA Sequences Custom Entities API
  slug: open-benchling-lims-custom-entities-api
- collection_type: open
  name: Benchling AA Sequences DNA Sequences API
  slug: open-benchling-lims-dna-sequences-api
- collection_type: open
  name: Benchling AA Sequences Entries API
  slug: open-benchling-lims-entries-api
- collection_type: open
  name: Benchling AA Sequences Events API
  slug: open-benchling-lims-events-api
- collection_type: open
  name: Benchling AA Sequences Inventory API
  slug: open-benchling-lims-inventory-api
- collection_type: open
  name: Benchling AA Sequences Lab Automation API
  slug: open-benchling-lims-lab-automation-api
- collection_type: open
  name: Benchling AA Sequences Molecules API
  slug: open-benchling-lims-molecules-api
- collection_type: open
  name: Benchling AA Sequences Oligos API
  slug: open-benchling-lims-oligos-api
- collection_type: open
  name: Benchling AA Sequences Projects & Folders API
  slug: open-benchling-lims-projects-folders-api
- collection_type: open
  name: Benchling AA Sequences Registry API
  slug: open-benchling-lims-registry-api
- collection_type: open
  name: Benchling AA Sequences Requests API
  slug: open-benchling-lims-requests-api
- collection_type: open
  name: Benchling AA Sequences RNA Sequences API
  slug: open-benchling-lims-rna-sequences-api
- collection_type: open
  name: Benchling AA Sequences Teams & Organizations API
  slug: open-benchling-lims-teams-organizations-api
- collection_type: open
  name: Benchling AA Sequences Users API
  slug: open-benchling-lims-users-api
- collection_type: open
  name: Benchling AA Sequences Workflows API
  slug: open-benchling-lims-workflows-api
- collection_type: open
  name: Benchling API
  slug: open-benchling-lims
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/benchling-lims-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/benchling-lims-agentic-access.yml
- group: auth
  title: ''
  type: TrustCenter
  url: security/benchling-lims-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/benchling-lims-domain-security.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/benchling-lims-authentication.yml
- group: auth
  title: ''
  type: OAuthScopes
  url: scopes/benchling-lims-scopes.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/benchling
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/benchling
- group: company
  title: ''
  type: Website
  url: https://www.benchling.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.benchling.com/docs/developer-platform-overview
- group: commercial
  title: ''
  type: Plans
  url: plans/benchling-lims-plans-pricing.yml
- group: operate
  title: ''
  type: RateLimits
  url: rate-limits/benchling-lims-rate-limits.yml
- group: commercial
  title: ''
  type: FinOps
  url: finops/benchling-lims-finops.yml
- group: company
  title: ''
  type: Blog
  url: https://www.benchling.com/blog
created: '2026-07-04'
description: Benchling is a life-sciences R&D cloud - a unified LIMS, electronic lab notebook (ELN), molecular biology registry, sample inventory, and workflow platform for biotech and pharma. Its tenant-scoped REST API (v2) exposes the same objects scientists work with in the UI - DNA/RNA/protein sequences, custom entities and the registry, inventory (boxes, locations, containers, plates), notebook entries, assay results and runs, lab-automation transforms, workflow tasks, and requests - plus events and webhooks for event-driven automation.
finops:
- name: Benchling Lims Finops
  service_category: Life Sciences R&D Platform (LIMS / ELN)
  slug: benchling-lims-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/benchling-lims.png
layout: provider
modified: '2026-07-04'
name: Benchling
nav: Providers
network: true
overview: 'Benchling publishes 20 APIs on the [APIs.io](https://apis.io/) network, including AA Sequences API, Apps API, Assay Results API, and 17 more. Tagged areas include Life Sciences, Biotech, LIMS, Electronic Lab Notebook, and Registry.


  Benchling''s developer surface includes authentication, documentation, engineering blog, and 11 more developer resources.'
plans:
- name: Benchling Lims Plans Pricing
  plan_count: 4
  slug: benchling-lims-plans-pricing
random_paper: 13
rate_limits:
- limit_count: 4
  name: Benchling Lims Rate Limits
  slug: benchling-lims-rate-limits
scopes:
- name: Benchling Lims Scopes
  scope_count: 0
  slug: benchling-lims-scopes
  summary_line: OAuth 2.0 · no documented scopes
score:
  band: developing
  composite: 40.6
  coverage:
    artifact_dirs: 11
    catalog_earned: 61.0
    catalog_earned_first_party: 0.0
    catalog_gap: 54.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: -0.7
  facets:
    access_clarity: 47.4
    commercial_clarity: 47.4
    contract_governance: 0.0
    contract_quality: 46.0
    developer_ergonomics: 23.8
    discoverability: 63.0
    governance: 0.0
    operational_transparency: 38.2
  previous_composite: 41.3
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 20
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 42.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/benchling-lims/refs/heads/main/screenshots/benchling-lims-2026-07-25T202730.png
security:
- kind: authentication
  name: Benchling Lims Authentication
  slug: benchling-lims-authentication
  summary_line: http/oauth2 · 2 schemes
- kind: domain-security
  name: Benchling Lims Domain Security
  slug: benchling-lims-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Benchling Lims Trust Center
  slug: benchling-lims-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, GDPR
slug: benchling-lims
tags:
- Life Sciences
- Biotech
- LIMS
- Electronic Lab Notebook
- Registry
- Molecular Biology
- Inventory Management
- Assay Management
- Workflows
- Webhook
- REST
website: https://www.benchling.com
---
