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
api_count: 0
artifact_total: 1
common:
- group: company
  title: ''
  type: Website
  url: https://www.latticehealthai.com/
- group: operate
  title: ''
  type: Contact
  url: mailto:christine@latticehealthai.com
- group: other
  title: ''
  type: VentureCapital
  url: https://www.ycombinator.com/companies/lattice-health
- group: auth
  title: ''
  type: DomainSecurity
  url: security/lattice-health-domain-security.yml
- group: agent
  title: ''
  type: WellKnownProbe
  url: well-known/lattice-health-well-known.yml
- group: design
  title: ''
  type: Conformance
  url: conformance/lattice-health-conformance.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: llms/lattice-health-llms.txt
created: '2026-07-17'
description: Lattice Health is a Y Combinator (Spring 2026) healthcare company building AI governance as a managed service for hospitals. The platform sits beside an existing clinical stack and taps the HL7 and DICOM signals that deployed imaging and clinical AI models already emit, with no rip-and-replace integration, then continuously measures population drift (PSI), subgroup fairness disparity under HHS Section 1557, latency against target, and silent vendor model-update detection across every vendor model running in production. Rather than another dashboard, Lattice delivers a per-role signed PDF report each morning to IT directors, CMIO/CIO, and compliance officers, cryptographically signed with the institution's own signing key so any recipient, including outside counsel or a regulator, can verify the artifact offline with standard open-source tooling and no Lattice account or infrastructure. Radiologist thumbs-up/thumbs-down feedback on AI results is aggregated at model level and
  folded into the next morning's findings. The company positions itself around standards alignment (IHE UPS-RS work-list status, AI-Results and ERA classification, ONC HTI-1, FDA Predetermined Change Control Plan envelopes with automatic breach detection) and HIPAA-safe egress with a strict-mode PHI redactor, deployed on-premise or in the customer's private cloud so PHI stays behind the hospital firewall. As of this profile Lattice Health publishes no public developer portal, API documentation, machine-readable API specification, SDKs, or pricing; it is a pre-public-API company tracked here as an AI governance and clinical AI oversight lead.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/lattice-health.png
layout: provider
modified: '2026-07-19'
name: Lattice Health
nav: Providers
network: true
overview: Lattice Health is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Company, Healthcare, Health IT, Artificial Intelligence, and AI Governance.
random_paper: 10
score:
  band: minimal
  composite: 5.0
  delta: -1.9
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 0.0
    discoverability: 57.4
    governance: 0.0
    operational_transparency: 0.0
  previous_composite: 6.9
  provenance:
    conformance: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 13.8
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/lattice-health/refs/heads/main/screenshots/lattice-health-2026-07-25T224608.png
security:
- kind: domain-security
  name: Lattice Health Domain Security
  slug: lattice-health-domain-security
  summary_line: TLSv1.3 · HSTS
slug: lattice-health
tags:
- Company
- Healthcare
- Health IT
- Artificial Intelligence
- AI Governance
- Clinical AI
- Medical Imaging
- Radiology
- DICOM
- HL7
- Compliance
- Monitoring
- Observability
website: https://www.latticehealthai.com/
---
