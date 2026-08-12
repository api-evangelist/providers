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
    openapi_examples: documented
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 4.7
  scored_at: '2026-08-11'
api_count: 5
apis:
- description: The foundational specification of the Zero Trust security model. Defines the seven tenets, the PDP/PEP/PA logical components, and the deployment variants (enhanced identity governance, microsegmentati
  name: NIST SP 800-207 Zero Trust Architecture
  slug: nist-sp-800-207
- description: CISA's Zero Trust Maturity Model defines four maturity levels (Traditional, Initial, Advanced, Optimal) across five pillars (Identity, Devices, Networks, Applications & Workloads, Data) and three cros
  name: CISA Zero Trust Maturity Model
  slug: cisa-zero-trust-maturity-model
- description: The Department of Defense Zero Trust Reference Architecture defines the seven DoD Zero Trust pillars (User, Device, Application & Workload, Data, Network & Environment, Automation & Orchestration, Vis
  name: DoD Zero Trust Reference Architecture
  slug: dod-zero-trust-reference-architecture
- description: A series of NSA Cybersecurity Information Sheets providing pillar-by- pillar guidance for implementing Zero Trust, including the Network and Environment, User, Device, Application & Workload, and Data
  name: NSA Zero Trust Guidance
  slug: nsa-zero-trust-guidance
- description: The UK National Cyber Security Centre's eight Zero Trust design principles, providing the British government's view of Zero Trust architecture for both public-sector and private organizations.
  name: UK NCSC Zero Trust Architecture Design Principles
  slug: ncsc-zero-trust-principles
artifact_total: 30
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zero-trust-security-model-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zero-trust-security-model-domain-security.yml
- group: docs
  title: NIST Zero Trust Architecture
  type: Documentation
  url: https://www.nist.gov/publications/zero-trust-architecture
- group: docs
  title: NIST SP 800-207 PDF
  type: Documentation
  url: https://nvlpubs.nist.gov/nistpubs/specialpublications/NIST.SP.800-207.pdf
- group: docs
  title: NIST SP 800-207A PDF
  type: Documentation
  url: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-207A.pdf
- group: auth
  title: CISA Zero Trust Maturity Model
  type: Compliance
  url: https://www.cisa.gov/zero-trust-maturity-model
- group: auth
  title: OMB M-22-09 Federal Zero Trust Strategy
  type: Compliance
  url: https://www.whitehouse.gov/wp-content/uploads/2022/01/M-22-09.pdf
- group: auth
  title: DoD Zero Trust Reference Architecture
  type: Compliance
  url: https://dodcio.defense.gov/Portals/0/Documents/Library/ZT-Reference-Architecture.pdf
- group: docs
  title: NSA Zero Trust Guidance
  type: Documentation
  url: https://www.nsa.gov/Press-Room/News-Highlights/Article/Article/2899282/nsa-releases-guidance-on-zero-trust-security-model/
- group: docs
  title: UK NCSC Zero Trust
  type: Documentation
  url: https://www.ncsc.gov.uk/collection/zero-trust-architecture
- group: start
  title: Cloudflare Learning - What Is Zero Trust
  type: Portal
  url: https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/
- group: start
  title: Microsoft Zero Trust Guidance Center
  type: Portal
  url: https://learn.microsoft.com/en-us/security/zero-trust/
- group: start
  title: Google BeyondCorp
  type: Portal
  url: https://cloud.google.com/beyondcorp
- group: build
  title: SPIFFE
  type: GitHubOrganization
  url: https://github.com/spiffe
- group: build
  title: Open Policy Agent
  type: GitHubOrganization
  url: https://github.com/open-policy-agent
- group: docs
  title: Zero Trust Pillar Schema
  type: JSONSchema
  url: json-schema/zero-trust-security-model-pillar-schema.json
- group: docs
  title: Zero Trust Maturity Assessment Schema
  type: JSONSchema
  url: json-schema/zero-trust-security-model-maturity-schema.json
- group: design
  title: Zero Trust Pillar Structure
  type: JSONStructure
  url: json-structure/zero-trust-security-model-pillar-structure.json
- group: design
  title: Zero Trust Security Model JSON-LD Context
  type: JSONLD
  url: json-ld/zero-trust-security-model-context.jsonld
- group: build
  title: Zero Trust Maturity Assessment Example
  type: CodeExamples
  url: examples/zero-trust-security-model-maturity-example.json
- group: other
  title: Zero Trust Security Model Vocabulary
  type: Resources
  url: vocabulary/zero-trust-security-model-vocabulary.yaml
created: '2025'
description: The Zero Trust security model is a strategic cybersecurity approach that eliminates implicit trust and requires continuous verification of every user, device, workload, and request attempting to access resources, regardless of network location. It is rooted in NIST SP 800-207, formalized for federal agencies by the CISA Zero Trust Maturity Model and the DoD Zero Trust Reference Architecture, and operationalized by NSA, NCSC, and industry guidance. This topic indexes the canonical specifications, guidance documents, advocacy organizations, and reference data schemas that describe the Zero Trust security model and its pillars (Identity, Devices, Networks, Applications & Workloads, Data, Visibility & Analytics, Automation & Orchestration).
examples:
- key_count: 6
  name: Zero Trust Security Model Maturity Example
  slug: zero-trust-security-model-maturity-example
features:
- description: No user, device, or network is trusted by default; every access is verified.
  name: Never Trust Always Verify
- description: Authentication and authorization happen for every request using all available signals.
  name: Explicit Verification
- description: Users and workloads receive only the minimum permissions required for the task.
  name: Least Privilege Access
- description: The model is designed assuming attackers are already present in the environment.
  name: Assume Breach
- description: All sessions and signals are continuously analyzed and policies re-evaluated.
  name: Continuous Monitoring
- description: Networks and workloads are segmented to limit blast radius after compromise.
  name: Microsegmentation
- description: Security controls follow the data, not the perimeter.
  name: Data-Centric Protection
- description: User and workload identity replaces network location as the primary trust boundary.
  name: Identity as the Perimeter
finops:
- name: Zero Trust Security Model Finops
  service_category: API
  slug: zero-trust-security-model-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zero-trust-security-model.png
json_schemas:
- name: Zero Trust Maturity Assessment
  property_count: 6
  slug: zero-trust-security-model-maturity
- name: Zero Trust Pillar
  property_count: 5
  slug: zero-trust-security-model-pillar
json_structures:
- name: Zero Trust Security Model Pillar Structure
  property_count: 5
  slug: zero-trust-security-model-pillar-structure
jsonld:
- class_count: 19
  name: Zero Trust Security Model Context
  property_count: 0
  slug: zero-trust-security-model-context
layout: provider
modified: '2026-05-03'
name: Zero-Trust Security Model
nav: Providers
network: true
overview: 'Zero-Trust Security Model publishes 5 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Access Control, Cybersecurity, Federal, Identity Management, and Network Security.


  The Zero-Trust Security Model catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Zero-Trust Security Model''s developer surface includes documentation, developer portal, code examples, and 18 more developer resources.'
plans:
- name: Zero Trust Security Model Plans Pricing
  plan_count: 3
  slug: zero-trust-security-model-plans-pricing
random_paper: 26
rate_limits:
- limit_count: 5
  name: Zero Trust Security Model Rate Limits
  slug: zero-trust-security-model-rate-limits
rules:
- name: Zero-Trust Security Model API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 4
  slug: zero-trust-security-model-jsonschema-spectral-rules
score:
  band: thin
  composite: 29.4
  delta: -6.6
  facets:
    commercial_clarity: 23.7
    contract_quality: 12.9
    developer_ergonomics: 17.4
    discoverability: 72.2
    governance: 58.3
    operational_transparency: 13.2
  previous_composite: 36.0
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 40.7
  schema_version: 0.11.0
  scored_at: '2026-08-11'
  trend: falling
screenshot: https://raw.githubusercontent.com/api-evangelist/zero-trust-security-model/refs/heads/main/screenshots/zero-trust-security-model-2026-06-20T201831.png
security:
- kind: domain-security
  name: Zero Trust Security Model Domain Security
  slug: zero-trust-security-model-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Zero Trust Security Model Vulnerability Disclosure
  slug: zero-trust-security-model-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: zero-trust-security-model
tags:
- Access Control
- Cybersecurity
- Federal
- Identity Management
- Network Security
- NIST
- Security
- Security Framework
- Zero Trust
use_cases:
- description: Meeting OMB M-22-09 and CISA Zero Trust Maturity Model requirements.
  name: Federal Civilian Compliance
- description: Implementing the seven DoD Zero Trust pillars and 152 capabilities.
  name: DoD Mission Systems
- description: Applying Zero Trust to OT and ICS environments in energy, water, and transportation.
  name: Critical Infrastructure
- description: Protecting PHI under HIPAA using Zero Trust controls and continuous verification.
  name: Healthcare Data Protection
- description: Aligning Zero Trust with SOX, GLBA, and PCI-DSS requirements.
  name: Financial Services Compliance
- description: Securing distributed research networks and BYOD environments.
  name: Higher Education Research
website: https://www.cloudflare.com/learning/security/glossary/what-is-zero-trust/
---
