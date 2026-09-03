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
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 25.8
  scored_at: '2026-09-03'
agentic_access:
- acting_count: 0
  human_in_the_loop: 0
  name: Apache Software Foundation Agentic Access
  operation_count: 14
  slug: apache-software-foundation-agentic-access
  summary_line: 14 operations
api_count: 1
apis:
- baseURL: https://whimsy.apache.org/public
  baseurl_source: spec
  description: The Committees API from Apache Software Foundation — 3 operation(s) for committees.
  name: Apache Software Foundation Committees API
  slug: apache-software-foundation-committees-api
- baseURL: https://whimsy.apache.org/public
  baseurl_source: spec
  description: The Groups API from Apache Software Foundation — 1 operation(s) for groups.
  name: Apache Software Foundation Groups API
  slug: apache-software-foundation-groups-api
- baseURL: https://whimsy.apache.org/public
  baseurl_source: spec
  description: The ICLA API from Apache Software Foundation — 1 operation(s) for icla.
  name: Apache Software Foundation ICLA API
  slug: apache-software-foundation-icla-api
- baseURL: https://whimsy.apache.org/public
  baseurl_source: spec
  description: The Members API from Apache Software Foundation — 1 operation(s) for members.
  name: Apache Software Foundation Members API
  slug: apache-software-foundation-members-api
- baseURL: https://whimsy.apache.org/public
  baseurl_source: spec
  description: The People API from Apache Software Foundation — 3 operation(s) for people.
  name: Apache Software Foundation People API
  slug: apache-software-foundation-people-api
- baseURL: https://whimsy.apache.org/public
  baseurl_source: spec
  description: The Podlings API from Apache Software Foundation — 2 operation(s) for podlings.
  name: Apache Software Foundation Podlings API
  slug: apache-software-foundation-podlings-api
artifact_total: 47
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Apache Software Foundation Projects Committees API
  slug: open-apache-software-foundation-committees-api
- collection_type: open
  name: Apache Software Projects Committees Foundation API
  slug: open-apache-software-foundation-foundation-api
- collection_type: open
  name: Apache Software Foundation Projects Committees Groups API
  slug: open-apache-software-foundation-groups-api
- collection_type: open
  name: Apache Software Foundation Projects Committees ICLA API
  slug: open-apache-software-foundation-icla-api
- collection_type: open
  name: Apache Software Foundation Projects Committees Members API
  slug: open-apache-software-foundation-members-api
- collection_type: open
  name: Apache Software Foundation Projects Committees People API
  slug: open-apache-software-foundation-people-api
- collection_type: open
  name: Apache Software Foundation Projects Committees Podlings API
  slug: open-apache-software-foundation-podlings-api
- collection_type: open
  name: Apache Software Foundation Committees Projects API
  slug: open-apache-software-foundation-projects-api
- collection_type: open
  name: Apache Software Foundation Projects Committees Releases API
  slug: open-apache-software-foundation-releases-api
- collection_type: open
  name: Apache Software Foundation Whimsy Public Data API
  slug: open-apache-software-foundation-whimsy-api
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/apache-software-foundation-agentic-access.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-software-foundation-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-software-foundation-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-apache-software-foundation
- group: start
  title: ''
  type: Portal
  url: https://www.apache.org/
- group: company
  title: ''
  type: Blog
  url: https://blogs.apache.org/
- group: docs
  title: ''
  type: Documentation
  url: https://www.apache.org/foundation/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: design
  title: ''
  type: SpectralRules
  url: rules/apache-software-foundation-spectral-rules.yml
- group: design
  title: ''
  type: Vocabulary
  url: vocabulary/apache-software-foundation-vocabulary.yaml
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
created: '2025-01-01'
description: APIs for the Apache Software Foundation (ASF), a nonprofit organization that supports the development of open-source software projects under the Apache License, providing governance, legal protection, and infrastructure for over 350 projects. The ASF exposes public APIs for project discovery, committee governance data, member information, and organizational structure through its Projects API and Whimsy Public Data API.
examples:
- key_count: 9
  name: Apache Software Foundation Committee Example
  slug: apache-software-foundation-committee-example
- key_count: 10
  name: Apache Software Foundation Podling Example
  slug: apache-software-foundation-podling-example
- key_count: 12
  name: Apache Software Foundation Project Example
  slug: apache-software-foundation-project-example
features:
- description: Comprehensive directory of all 350+ ASF top-level projects with metadata.
  name: Project Directory
- description: Project Management Committee membership, chair, and governance information.
  name: Committee Data
- description: Apache Incubator podling status, mentors, and graduation tracking.
  name: Podling Tracking
- description: Release version and date history for all ASF projects.
  name: Release History
- description: Public member, committer, and ICLA data from the ASF Whimsy system.
  name: Whimsy Member Data
finops:
- name: Apache Software Foundation Finops
  service_category: API
  slug: apache-software-foundation-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-software-foundation.png
integrations:
- description: All ASF project repositories hosted under the apache GitHub organization.
  name: Apache GitHub Organization
- description: Issue tracking at issues.apache.org for all ASF project bug reports and features.
  name: ASF JIRA
- description: Wiki documentation at cwiki.apache.org for ASF project and foundation docs.
  name: Apache Confluence
json_schemas:
- name: Apache Software Foundation Committee
  property_count: 9
  slug: apache-software-foundation-committee
- name: Apache Software Foundation Podling
  property_count: 10
  slug: apache-software-foundation-podling
- name: Apache Software Foundation Project
  property_count: 12
  slug: apache-software-foundation-project
json_structures:
- name: Apache Software Foundation Committee Structure
  property_count: 9
  slug: apache-software-foundation-committee-structure
- name: Apache Software Foundation Podling Structure
  property_count: 10
  slug: apache-software-foundation-podling-structure
- name: Apache Software Foundation Project Structure
  property_count: 12
  slug: apache-software-foundation-project-structure
jsonld:
- class_count: 5
  name: Apache Software Foundation Asf Context
  property_count: 22
  slug: apache-software-foundation-asf-context
layout: provider
modified: '2026-05-19'
name: Apache Software Foundation
nav: Providers
network: true
overview: 'Apache Software Foundation publishes 6 APIs on the [APIs.io](https://apis.io/) network, including Committees API, Groups API, ICLA API, and 3 more. Tagged areas include ASF, Open-Source, Governance, Project, and Apache.


  The Apache Software Foundation catalog on APIs.io includes 1 JSON-LD context and 2 Spectral governance rulesets.


  Apache Software Foundation''s developer surface includes developer portal, engineering blog, documentation, and 8 more developer resources.'
plans:
- name: Apache Software Foundation Plans Pricing
  plan_count: 3
  slug: apache-software-foundation-plans-pricing
random_paper: 8
rate_limits:
- limit_count: 5
  name: Apache Software Foundation Rate Limits
  slug: apache-software-foundation-rate-limits
rules:
- effective_rule_count: 5
  extends: []
  name: Apache Software Foundation API Rules
  rule_count: 5
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 3
  slug: apache-software-foundation-jsonschema-spectral-rules
- effective_rule_count: 63
  extends:
  - spectral:oas
  name: Apache Software Foundation API Rules
  rule_count: 22
  severity_counts:
    error: 8
    hint: 0
    info: 3
    warn: 11
  slug: apache-software-foundation-spectral-rules
score:
  band: thin
  composite: 35.7
  coverage:
    artifact_dirs: 15
    catalog_gap: 44.5
    catalog_max: 100.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 28.6
    commercial_clarity: 28.6
    contract_governance: 28.8
    contract_quality: 59.9
    developer_ergonomics: 21.4
    discoverability: 59.3
    governance: 28.8
    operational_transparency: 10.5
  previous_composite: 35.7
  provenance:
    agentic_access: derived
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 9
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-software-foundation/refs/heads/main/screenshots/apache-software-foundation-2026-06-20T172144.png
security:
- kind: domain-security
  name: Apache Software Foundation Domain Security
  slug: apache-software-foundation-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Software Foundation Vulnerability Disclosure
  slug: apache-software-foundation-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-software-foundation
tags:
- ASF
- Open-Source
- Governance
- Project
- Apache
use_cases:
- description: Discover and explore all Apache Software Foundation projects programmatically.
  name: Apache Project Discovery
- description: Access committee membership and governance data for ASF organizational research.
  name: Governance Transparency
- description: Track release histories and versions across all ASF projects.
  name: Release Monitoring
- description: Monitor Apache Incubator podlings and their progression to top-level projects.
  name: Incubator Tracking
website: https://www.apache.org/
---
