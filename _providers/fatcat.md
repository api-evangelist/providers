---
access_model:
  confidence: high
  label: Free · Self-serve signup
  onboarding: self-serve
  pricing: free
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
    auth_clarity: true
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 30.6
  scored_at: '2026-08-03'
agentic_access:
- acting_count: 42
  human_in_the_loop: 0
  name: Fatcat Agentic Access
  operation_count: 96
  slug: fatcat-agentic-access
  summary_line: 96 operations · 42 acting
api_count: 11
apis:
- description: 'Helper methods and internal APIs for editor authentication. # TAGLINE'
  name: Fatcat auth API
  slug: fatcat-auth-api
- description: 'The **Changelog** is the ordered feed of editgroups which have been # TAGLINE accepted into the catalog. # TAGLINE'
  name: Fatcat changelog API
  slug: fatcat-changelog-api
- description: '**Container** entities represent publication venues like journals, # TAGLINE conference proceedings, book series, or blogs. They group publications # TAGLINE ("releases"). # TAGLINE See the "Catalog S'
  name: Fatcat containers API
  slug: fatcat-containers-api
- description: '**Creator** entities represent individuals (or organizations, or other # TAGLINE agents) who contribute to the creation of specific releases # TAGLINE (publications). # TAGLINE See the "Catalog Style '
  name: Fatcat creators API
  slug: fatcat-creators-api
- description: '**Editgroups** are sets of changes, each to individual entities in the # TAGLINE catalog. Every edit must be part of an editgroup which is reviewed and # TAGLINE accepted (merged) as a whole. # TAGLIN'
  name: Fatcat editgroups API
  slug: fatcat-editgroups-api
- description: '**Editors** are human user accounts and bots that make changes to the # TAGLINE Fatcat catalog. # TAGLINE The API allows fetching (and updating) metadata about individual editors, # TAGLINE as well as'
  name: Fatcat editors API
  slug: fatcat-editors-api
- description: '**File** entities represent unique digital files which are full # TAGLINE manifestations of specific releases (publications), such as fulltext PDF # TAGLINE files, JATS XML documents, or video files. '
  name: Fatcat files API
  slug: fatcat-files-api
- description: '**Fileset** entities represent sets of digital files, as well as locations # TAGLINE where they can be found on the public web. Filesets most commonly # TAGLINE represent datasets consisting of severa'
  name: Fatcat filesets API
  slug: fatcat-filesets-api
- description: '**Release** entities represent specific published versions of a research # TAGLINE work, such as a pre-print, a journal article, a book (or chapter), or a # TAGLINE scholarly blog post. Releases are a'
  name: Fatcat releases API
  slug: fatcat-releases-api
- description: '**Web Capture** entities represent archival snapshots of web pages (or # TAGLINE other web resources), which are usually complete manifestations of a # TAGLINE specific release entity. Web Captures al'
  name: Fatcat webcaptures API
  slug: fatcat-webcaptures-api
- description: '**Work** entities group several Release entities which are different # TAGLINE versions of the same abstract piece of research. For example, three # TAGLINE release entities representing the pre-print'
  name: Fatcat works API
  slug: fatcat-works-api
artifact_total: 28
common:
- group: agent
  title: ''
  type: AgenticAccess
  url: agentic-access/fatcat-agentic-access.yml
- group: auth
  title: ''
  type: Authentication
  url: authentication/fatcat-authentication.yml
created: '2026-06-13'
description: Fatcat is a versioned, user-editable open catalog of published research works maintained by the Internet Archive. It tracks bibliographic metadata, links papers to full-text copies, and preserves access to scholarly publications including journal articles, conference proceedings, and datasets across millions of research works.
examples:
- key_count: 12
  name: Container Entity Example
  slug: container-entity-example
- key_count: 9
  name: Creator Entity Example
  slug: creator-entity-example
- key_count: 7
  name: Editgroup Example
  slug: editgroup-example
- key_count: 11
  name: File Entity Example
  slug: file-entity-example
- key_count: 21
  name: Release Entity Example
  slug: release-entity-example
finops:
- name: Finops
  service_category: ''
  slug: finops
image: https://fatcat.wiki/static/fatcat_logo.svg
json_schemas:
- name: ContainerEntity
  property_count: 13
  slug: container-entity
- name: CreatorEntity
  property_count: 10
  slug: creator-entity
- name: Editgroup
  property_count: 8
  slug: editgroup
- name: FileEntity
  property_count: 13
  slug: file-entity
- name: ReleaseEntity
  property_count: 26
  slug: release-entity
jsonld:
- class_count: 8
  name: context Context
  property_count: 65
  slug: context
layout: provider
modified: '2026-06-13'
name: Fatcat
nav: Providers
network: true
overview: 'Fatcat publishes 11 APIs on the [APIs.io](https://apis.io/) network, including auth API, changelog API, containers API, and 8 more. Tagged areas include Scholarly, Research, Academic, Open Access, and Bibliographic.


  The Fatcat catalog on APIs.io includes 1 JSON-LD context and 1 Spectral governance ruleset.


  Fatcat''s developer surface includes authentication and 1 more developer resources.'
plans:
- name: Plans
  plan_count: 1
  slug: plans
random_paper: 57
rate_limits:
- limit_count: 0
  name: Rate Limits
  slug: rate-limits
rules:
- name: Fatcat API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 1
    warn: 5
  slug: fatcat-jsonschema-spectral-rules
score:
  band: thin
  composite: 35.6
  delta: 0.0
  facets:
    commercial_clarity: 28.9
    contract_quality: 50.0
    developer_ergonomics: 10.9
    discoverability: 81.5
    governance: 58.3
    operational_transparency: 0.0
  previous_composite: 35.6
  provenance:
    agentic_access: derived
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 11
  schema_version: 0.9
  scored_at: '2026-08-03'
  trend: flat
security:
- kind: authentication
  name: Fatcat Authentication
  slug: fatcat-authentication
  summary_line: apiKey · 1 scheme
slug: fatcat
tags:
- Scholarly
- Research
- Academic
- Open Access
- Bibliographic
- Publications
- Metadata
- Internet Archive
website: https://fatcat.wiki/
---
