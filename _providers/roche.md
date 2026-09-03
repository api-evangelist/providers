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
  scored_at: '2026-09-02'
api_count: 0
artifact_total: 13
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/roche-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/roche-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/roche
- group: company
  title: ''
  type: Website
  url: https://www.roche.com/
- group: build
  title: ''
  type: GitHubOrg
  url: https://github.com/Roche
- group: start
  title: ''
  type: DiagnosticsPortal
  url: https://diagnostics.roche.com/
- group: other
  title: ''
  type: NavifyPlatform
  url: https://navify.roche.com/
- group: start
  title: ''
  type: SuppliersPortal
  url: https://suppliers.roche.com/
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/roche-vocabulary.yml
- group: other
  title: ''
  type: ProductPage
  url: https://github.com/Roche/pyreadstat
- group: other
  title: ''
  type: ProductPage
  url: https://github.com/Roche/foxops
- group: other
  title: ''
  type: ProductPage
  url: https://github.com/Roche/OligoGym
created: '2026-05-05'
description: 'F. Hoffmann-La Roche is a Swiss multinational healthcare company with two divisions: Roche Pharma and Roche Diagnostics. Roche does not publish a general public developer API but exposes interoperability through the navify diagnostics platform, the cobas infinity laboratory software, and an open-source GitHub presence focused on data-science tooling such as pyreadstat, foxops, and OligoGym.'
features:
- description: pyreadstat reads/writes SAS, SPSS, and Stata files used in regulated clinical studies
  name: Clinical Data File Interop
- description: foxops keeps repo templates synchronized across an org with a REST service
  name: GitOps Templating
- description: OligoGym provides featurization and modeling for nucleic-acid therapeutics
  name: Oligonucleotide ML Toolkit
- description: navify provides Roche Diagnostics digital and algorithm services
  name: Diagnostics Platform
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/roche.png
integrations:
- description: pyreadstat integrates with both major Python dataframe libraries
  name: pandas and polars
- description: foxops integrates with GitLab and provides a Terraform provider
  name: GitLab and Terraform
- description: Roche Diagnostics participates in healthcare interoperability standards
  name: HL7 / FHIR
jsonld:
- class_count: 8
  name: Roche Context
  property_count: 0
  slug: roche-context
layout: provider
modified: '2026-07-25'
name: Roche
nav: Providers
network: true
overview: 'Roche is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceuticals, Biotechnology, Healthcare, and Diagnostics.


  The Roche catalog on APIs.io includes 1 JSON-LD context.'
random_paper: 4
score:
  band: minimal
  composite: 9.6
  coverage:
    artifact_dirs: 7
    catalog_gap: 80.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 0.0
    commercial_clarity: 0.0
    contract_governance: 15.2
    contract_quality: 10.7
    developer_ergonomics: 0.0
    discoverability: 40.7
    governance: 15.2
    operational_transparency: 5.3
  previous_composite: 9.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Health
    regime_id: health
    score: 21.3
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/roche/refs/heads/main/screenshots/roche-2026-06-20T193147.png
security:
- kind: domain-security
  name: Roche Domain Security
  slug: roche-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Roche Vulnerability Disclosure
  slug: roche-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: roche
tags:
- Pharmaceuticals
- Biotechnology
- Healthcare
- Diagnostics
use_cases:
- description: Load SAS/SPSS/Stata files from clinical trials into modern Python pipelines
  name: Clinical Data Ingestion
- description: Roll out consistent CI/CD and project scaffolds across many repos
  name: Repository Standardization
- description: Predict oligonucleotide properties to support drug discovery research
  name: Therapeutic Discovery
website: https://www.roche.com/
---
