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
    agent_skills: false
    agentic_access: false
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.1
  score: 0.0
  scored_at: '2026-07-23'
api_count: 3
apis:
- description: pyreadstat is Roche's Apache 2.0 Python package for reading and writing SAS (sas7bdat), SPSS, and Stata files into pandas and polars data frames. Widely used in clinical and life-sciences data pipelin
  name: Roche pyreadstat
  slug: pyreadstat
- description: foxops is Roche's open-source templating system for Git repositories, with a REST API service, Python client, and Terraform provider. Used to keep repository scaffolding in sync across an organization
  name: Roche foxops
  slug: foxops
- description: OligoGym streamlines featurization, training, and evaluation of predictive models for oligonucleotide properties. Apache 2.0.
  name: Roche OligoGym
  slug: oligogym
artifact_total: 16
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
modified: '2026-05-16'
name: Roche
nav: Providers
network: true
overview: 'Roche publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Pharmaceutical, Biotechnology, Healthcare, and Diagnostics.


  The Roche catalog on APIs.io includes 1 JSON-LD context.'
random_paper: 19
score:
  band: emerging
  composite: 17.1
  delta: 3.6
  facets:
    commercial_clarity: 0.0
    contract_quality: 15.1
    developer_ergonomics: 0.0
    discoverability: 75.0
    governance: 13.2
    operational_transparency: 5.3
  previous_composite: 13.5
  regulatory:
    applies: true
    regime: Health
    regime_id: health
    score: 37.0
  schema_version: 0.5
  scored_at: '2026-07-23'
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
- Pharmaceutical
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
