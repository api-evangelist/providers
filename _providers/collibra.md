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
  scored_at: '2026-07-27'
api_count: 7
apis:
- description: 'The Collibra Core REST API exposes the full Collibra Platform for programmatic management of communities, domains, assets, relations, attributes, tags, comments, workflows, and policies. The API uses '
  name: Collibra Core REST API
  slug: collibra-core-rest-api
- description: The Knowledge Graph GraphQL API enables retrieval of Collibra assets, relations, communities, domains, and complex multi-hop relations in a single query. Designed for analytical and AI pipeline use ca
  name: Collibra Knowledge Graph GraphQL API
  slug: collibra-knowledge-graph-graphql-api
- description: Collibra Data Quality and Observability APIs manage quality rules, monitoring jobs, dataset profiles, anomalies, and remediation workflows. Supports natural-language and code-defined quality checks ac
  name: Collibra Data Quality and Observability API
  slug: collibra-data-quality-observability-api
- description: The Data Lineage API exposes end-to-end column-level and table-level data lineage across SQL warehouses, ETL pipelines, BI tools, and streaming systems for impact analysis and regulatory documentation
  name: Collibra Data Lineage API
  slug: collibra-data-lineage-api
- description: The Workflow API manages BPMN-based governance workflows including data steward review, access request, issue resolution, and asset promotion. Supports deployment, instance management, and event- driv
  name: Collibra Workflow API
  slug: collibra-workflow-api
- description: The Collibra AI Command Center provides a unified control plane for governing enterprise AI systems with continuous visibility, trust signals, automated traceability, and risk-based oversight of model
  name: Collibra AI Command Center
  slug: collibra-ai-command-center-api
- description: Collibra ships a broad library of source connectors for ingesting metadata from data warehouses, BI tools, cloud storage, streaming systems, and AI platforms including Snowflake, Databricks, BigQuery,
  name: Collibra Integration Connectors
  slug: collibra-integration-connectors
artifact_total: 32
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/collibra-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/collibra-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/collibra
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/collibra
- group: company
  title: ''
  type: Website
  url: https://www.collibra.com/
- group: start
  title: ''
  type: Portal
  url: https://developer.collibra.com/
- group: docs
  title: ''
  type: Documentation
  url: https://www.collibra.com/documentation
- group: operate
  title: ''
  type: Community
  url: https://community.collibra.com/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.collibra.com/pricing
created: '2026-05-05'
description: Collibra is a data intelligence company providing a cloud-based platform for data governance, cataloging, quality, lineage, and AI governance. The Collibra Data Intelligence Platform helps enterprises discover, understand, govern, and trust their data assets through automated lineage tracking, policy management, data observability, and collaborative stewardship. The Collibra developer ecosystem includes REST APIs, GraphQL Knowledge Graph API, workflow automation, and a broad library of source connectors.
features:
- description: Discover, document, and govern enterprise data assets across cloud and on-prem.
  name: Data Catalog
- description: Define policies, roles, and stewardship for data assets and metrics.
  name: Data Governance
- description: Automate data quality monitoring, anomaly detection, and remediation.
  name: Data Quality and Observability
- description: Column-level and table-level lineage across SQL, ETL, and BI systems.
  name: Data Lineage
- description: Govern AI models, agents, and AI-using applications with risk-based oversight.
  name: AI Governance
- description: BPMN-based stewardship workflows for review, access, and remediation.
  name: Workflow Automation
- description: Programmatic access to the full Collibra metadata graph.
  name: REST and GraphQL APIs
- description: Out-of-the-box ingestion for major data warehouses, BI tools, and cloud platforms.
  name: Connector Library
graphqls:
- description: The Knowledge Graph GraphQL API enables retrieval of Collibra assets, relations, communities, domains, and complex multi-hop relations in a single query. Designed for analytical and AI pipeline use ca
  name: Collibra GraphQL API
  slug: collibra-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/collibra.png
integrations:
- description: Native metadata ingestion and lineage from Snowflake Data Cloud.
  name: Snowflake
- description: Integration with Databricks Lakehouse and Unity Catalog for metadata and lineage.
  name: Databricks
- description: Metadata ingestion and lineage from BigQuery.
  name: Google BigQuery
- description: Connector for Redshift metadata and lineage.
  name: AWS Redshift
- description: BI lineage and metadata ingestion from Tableau dashboards and data sources.
  name: Tableau
- description: BI lineage and metadata ingestion from Power BI workspaces.
  name: Power BI
- description: Unstructured-data context engine integration for AI-ready data pipelines.
  name: Deasy Labs
- description: SAP enterprise application integration for metadata and master data governance.
  name: SAP
layout: provider
modified: '2026-05-16'
name: Collibra
nav: Providers
network: true
overview: 'Collibra publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Data Governance, Data Management, Data Catalog, Data Quality, and AI Governance.


  Collibra''s developer surface includes developer portal, documentation, pricing, and 6 more developer resources.'
random_paper: 24
score:
  band: emerging
  composite: 15.9
  delta: 0.0
  facets:
    commercial_clarity: 10.5
    contract_quality: 0.0
    developer_ergonomics: 21.7
    discoverability: 87.5
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 15.9
  schema_version: 0.5
  scored_at: '2026-07-27'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/collibra/refs/heads/main/screenshots/collibra-2026-06-20T174748.png
security:
- kind: domain-security
  name: Collibra Domain Security
  slug: collibra-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Collibra Vulnerability Disclosure
  slug: collibra-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: collibra
tags:
- Data Governance
- Data Management
- Data Catalog
- Data Quality
- AI Governance
- Data Lineage
- Enterprise Software
use_cases:
- description: Build a single catalog of governed data assets across business domains.
  name: Enterprise Data Catalog
- description: Document and demonstrate data lineage and controls for GDPR, BCBS 239, HIPAA, and other regulations.
  name: Regulatory Compliance
- description: Govern enterprise AI systems with continuous monitoring and audit trails.
  name: AI Risk Management
- description: Support federated domain ownership with central governance.
  name: Data Mesh Enablement
- description: Monitor and remediate data quality across pipelines and warehouses.
  name: Data Quality SLA Management
- description: Enable analysts and data scientists to find trusted, governed data.
  name: Self-Service Data Discovery
website: https://www.collibra.com/
---
