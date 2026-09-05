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
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-09-04'
api_count: 3
apis:
- description: 'The Sling Resource API provides RESTful access to JCR content repository nodes via HTTP. Every content node is addressable as a URL, supporting GET, POST, PUT, DELETE, and MOVE operations through the '
  name: Apache Sling Resource API
  slug: apache-sling-resource-api
- description: The Sling Scripting API enables server-side rendering through multiple scripting engines. Scripts are resolved from the content repository based on resource type and selectors, supporting HTL (HTML Te
  name: Apache Sling Scripting API
  slug: apache-sling-scripting-api
- description: The Sling Event API provides a job processing and eventing system built on OSGi EventAdmin. It supports distributed job queuing, scheduled job execution, event broadcasting across cluster nodes, and w
  name: Apache Sling Event API
  slug: apache-sling-event-api
artifact_total: 28
common:
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/sling/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/sling/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/sling/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-sling-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-sling-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache/sling-org-apache-sling-api
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/sling
- group: docs
  title: ''
  type: Documentation
  url: https://sling.apache.org/documentation.html
- group: start
  title: ''
  type: Portal
  url: https://sling.apache.org/
- group: start
  title: ''
  type: GettingStarted
  url: https://sling.apache.org/documentation/getting-started.html
- group: company
  title: ''
  type: Blog
  url: https://sling.apache.org/news.html
- group: operate
  title: ''
  type: Support
  url: https://sling.apache.org/project-information/mailing-lists.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/
- group: operate
  title: ''
  type: FAQ
  url: https://cwiki.apache.org/confluence/display/SLING/
- group: build
  title: Maven Central Packages
  type: SDKs
  url: https://search.maven.org/search?q=org.apache.sling
created: '2026-03-16'
description: Apache Sling is a RESTful web framework built on top of the Java Content Repository (JCR) standard. It maps HTTP requests to content resources using a resource-oriented URL decomposition model and uses scripts or servlets to render responses, supporting multiple scripting languages including HTL, JSP, Groovy, and server-side JavaScript. Apache Sling forms the foundation of Adobe Experience Manager (AEM) and is an Apache Software Foundation project with 300+ modular OSGi bundles.
features:
- description: Every JCR node is a REST resource accessible via URL with GET, POST, PUT, DELETE operations.
  name: Resource-Oriented REST API
- description: Flexible URL decomposition into resource path, selectors, extension, and suffix for content negotiation.
  name: URL Decomposition
- description: Powerful POST servlet for content CRUD operations, supporting create, modify, delete, move, copy, and import.
  name: SlingPostServlet
- description: Server-side rendering with HTL, JSP, Groovy, FreeMarker, Thymeleaf, and Rhino JavaScript.
  name: Multi-Language Scripting
- description: 300+ modular OSGi bundles with hot-deploy capability and dynamic configuration.
  name: OSGi Modular Architecture
- description: Sling Resource Type system enables component inheritance and script resolution.
  name: Resource Type Hierarchy
- description: Distributed job queue and event system for asynchronous content processing.
  name: Event and Job Processing
- description: Extensible health check system for monitoring Sling instance components.
  name: Health Check Framework
- description: Content distribution bundles for replicating content between Sling instances.
  name: Replication and Distribution
finops:
- name: Apache Sling Finops
  service_category: API
  slug: apache-sling-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-sling.png
integrations:
- description: Apache Sling is the foundational framework for Adobe Experience Manager (AEM).
  name: Adobe Experience Manager
- description: JCR implementation providing the content repository backend for Sling.
  name: Apache Jackrabbit Oak
- description: OSGi framework container that hosts Sling bundles and manages the service registry.
  name: Apache Felix
- description: OSGi runtime alternative for deploying Sling-based applications.
  name: Apache Karaf
- description: Maven plugin (slingstart-maven-plugin) and Maven archetypes for Sling development.
  name: Maven
- description: Search integration for indexing JCR content via Sling's indexing framework.
  name: Elasticsearch
layout: provider
modified: '2026-04-19'
name: Apache Sling
nav: Providers
network: true
overview: 'Apache Sling publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Content Management, Java, JCR, OSGi, and REST.


  Apache Sling''s developer surface includes documentation, developer portal, getting-started guide, engineering blog, support, FAQ, and 9 more developer resources.'
plans:
- name: Apache Sling Plans Pricing
  plan_count: 3
  slug: apache-sling-plans-pricing
random_paper: 20
rate_limits:
- limit_count: 5
  name: Apache Sling Rate Limits
  slug: apache-sling-rate-limits
score:
  band: emerging
  composite: 23.1
  coverage:
    artifact_dirs: 6
    catalog_earned: 44.0
    catalog_earned_first_party: 0.0
    catalog_gap: 71.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 40.0
  previous_composite: 23.1
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-sling/refs/heads/main/screenshots/apache-sling-2026-06-20T172143.png
security:
- kind: domain-security
  name: Apache Sling Domain Security
  slug: apache-sling-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Sling Vulnerability Disclosure
  slug: apache-sling-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-sling
tags:
- Content Management
- Java
- JCR
- OSGi
- REST
- Web Framework
- Open-Source
- Adobe Experience Manager
use_cases:
- description: Build REST-based CMS solutions with JCR-backed content repositories.
  name: Content Management Systems
- description: Foundation framework for AEM digital experience platform implementations.
  name: Adobe Experience Manager
- description: Serve structured JSON content via Sling's resource API for headless front-end applications.
  name: Headless CMS
- description: Build OSGi-based Java web applications with RESTful resource routing.
  name: Web Application Framework
- description: Manage and serve digital assets stored in JCR with metadata and rendition support.
  name: Digital Asset Management
website: https://sling.apache.org/
---
