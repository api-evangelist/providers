---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 20.0
  scored_at: '2026-09-01'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Federal Emergency Management Agency Agentic Access
  operation_count: 11
  slug: federal-emergency-management-agency-agentic-access
  summary_line: 11 operations
api_count: 1
apis:
- description: Public, individual, and hazard mitigation assistance
  name: Federal Emergency Management Agency Assistance API
  slug: federal-emergency-management-agency-assistance-api
- description: Disaster declarations and summaries
  name: Federal Emergency Management Agency Disasters API
  slug: federal-emergency-management-agency-disasters-api
- description: API and dataset metadata
  name: Federal Emergency Management Agency Metadata API
  slug: federal-emergency-management-agency-metadata-api
- description: National Flood Insurance Program data
  name: Federal Emergency Management Agency NFIP API
  slug: federal-emergency-management-agency-nfip-api
artifact_total: 17
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: OpenFEMA Assistance API
  slug: open-federal-emergency-management-agency-assistance-api
- collection_type: open
  name: OpenFEMA Assistance Disasters API
  slug: open-federal-emergency-management-agency-disasters-api
- collection_type: open
  name: OpenFEMA Assistance Metadata API
  slug: open-federal-emergency-management-agency-metadata-api
- collection_type: open
  name: OpenFEMA Assistance NFIP API
  slug: open-federal-emergency-management-agency-nfip-api
- collection_type: open
  name: OpenFEMA API
  slug: open-openfema
common:
- group: other
  title: ''
  type: CapabilityMap
  url: capabilities/federal-emergency-management-agency-capability-edges.yml
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/federal-emergency-management-agency-agentic-access.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/federal-emergency-management-agency-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/FEMA
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fema
- group: company
  title: ''
  type: Website
  url: https://www.fema.gov/
- group: docs
  title: ''
  type: Documentation
  url: https://www.fema.gov/about/openfema/api
created: '2024-12-03'
description: The Federal Emergency Management Agency (FEMA) coordinates the federal government's role in preparing for, preventing, mitigating, responding to, and recovering from disasters. The OpenFEMA program provides programmatic access to disaster declarations, public assistance, individual assistance, hazard mitigation, and National Flood Insurance Program (NFIP) data.
examples:
- key_count: 19
  name: Disaster Declaration
  slug: disaster-declaration
finops:
- name: Federal Emergency Management Agency Finops
  service_category: API
  slug: federal-emergency-management-agency-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/federal-emergency-management-agency.png
layout: provider
modified: '2026-05-19'
name: Federal Emergency Management Agency
nav: Providers
network: true
overview: 'Federal Emergency Management Agency publishes 4 APIs on the [APIs.io](https://apis.io/) network, including Assistance API, Disasters API, Metadata API, and 1 more. Tagged areas include Disasters, Emergencies, Federal-Government, Flood Insurance, and Hazard Mitigation.


  The Federal Emergency Management Agency catalog on APIs.io includes 1 Spectral governance ruleset.


  Federal Emergency Management Agency''s developer surface includes documentation and 6 more developer resources.'
plans:
- name: Federal Emergency Management Agency Plans Pricing
  plan_count: 3
  slug: federal-emergency-management-agency-plans-pricing
random_paper: 15
rate_limits:
- limit_count: 5
  name: Federal Emergency Management Agency Rate Limits
  slug: federal-emergency-management-agency-rate-limits
rules:
- effective_rule_count: 0
  extends: []
  name: Federal Emergency Management Agency API Rules
  rule_count: 0
  severity_counts:
    error: 0
    hint: 0
    info: 0
    warn: 0
  slug: openfema-rules
score:
  band: emerging
  composite: 20.6
  coverage:
    artifact_dirs: 11
    catalog_gap: 60.0
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 48.3
    developer_ergonomics: 9.5
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 20.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 4
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
security:
- kind: domain-security
  name: Federal Emergency Management Agency Domain Security
  slug: federal-emergency-management-agency-domain-security
  summary_line: TLSv1.3 · DNSSEC · DMARC
slug: federal-emergency-management-agency
tags:
- Disasters
- Emergencies
- Federal-Government
- Flood Insurance
- Hazard Mitigation
website: https://www.fema.gov/
---
