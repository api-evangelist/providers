---
aid: cmic
url: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/apis.yml
name: CMiC
x-type: company
tags:
  - Construction
  - ERP
  - Finance
  - Project Management
type: Index
image: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/image.png
access: 3rd-Party
created: '2026-03-18'
modified: '2026-04-23'
specificationVersion: '0.19'
description: CMiC is a unified construction-industry ERP and project management platform used by general contractors, civil contractors, and heavy/highway builders. CMiC exposes an OAuth 2.0 secured REST API (api.cmic.ca) along with a Power BI connector for accessing project financials, job costing, subcontractor and vendor management, equipment tracking, and document management with application-level security applied across company, job, project, and employee scopes.
apis:
  - aid: cmic:cmic-api
    name: CMiC Construction ERP API
    tags:
      - Construction
      - ERP
      - Finance
      - OAuth2
      - Project Management
    image: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/image.png
    humanURL: https://developers.cmicglobal.com/
    baseURL: https://api.cmic.ca
    properties:
      - url: https://developers.cmicglobal.com/docs/overview
        type: Documentation
      - url: https://developers.cmicglobal.com/v1/docs/authentication
        type: Authentication
      - url: https://developers.cmicglobal.com/docs/developer-api-account
        type: GettingStarted
      - url: https://docs.cmicglobal.com/portal/Content/E_Reference_Material/CMiC_API/Reference/API_and_OAuth2/API_and_OAuth2.htm
        type: Reference
      - url: openapi/cmic-construction-erp-openapi.yml
        type: OpenAPI
      - url: json-schema/cmic-project-schema.json
        type: JSONSchema
      - url: json-ld/cmic-context.jsonld
        type: JSONLDContext
      - url: rules/cmic-rules.yml
        type: SpectralRuleset
      - url: capabilities/cmic-construction-erp-capabilities.yml
        type: NaftikoCapabilities
    description: CMiC provides enterprise ERP and project management software for the construction industry. The REST API uses OAuth 2.0 (client credentials flow) with support for third-party identity providers like Microsoft Azure. APIs enable access to project financials, subcontractor management, job costing, equipment tracking, and document management. Application-level security is enforced across all endpoints respecting company, job, project, and employee access rules.
    x-features:
      - name: Project Management
        description: List, create, retrieve, and update construction projects.
      - name: Job Cost Tracking
        description: Track jobs, cost codes, budgets, and committed costs.
      - name: Subcontractor and Vendor Management
        description: List and manage vendors and subcontractors per company.
      - name: Equipment Tracking
        description: Track equipment, usage, and assignment.
      - name: Document Management
        description: List and retrieve project documents and approvals.
      - name: OAuth 2.0 Authentication
        description: Client credentials flow with Microsoft Azure / external IdP support.
    x-useCases:
      - name: Project Financials Dashboard
        description: Surface project, job, and cost-code data in BI tools.
      - name: Subcontractor Onboarding
        description: Sync vendor and subcontractor records into procurement systems.
      - name: Equipment Utilization
        description: Drive equipment-utilization reporting and predictive maintenance.
      - name: Document Workflow Automation
        description: Push and pull project documents into external review workflows.
  - aid: cmic:cmic-power-bi-connector
    name: CMiC API Power BI Connector
    tags:
      - Analytics
      - Business Intelligence
      - Construction
      - ERP
      - Power BI
    image: https://raw.githubusercontent.com/api-evangelist/cmic/refs/heads/main/image.png
    humanURL: https://docs.cmicglobal.com/portal/Content/Home.htm
    baseURL: https://api.cmic.ca
    properties:
      - url: https://docs.cmicglobal.com/portal/Content/Home.htm
        type: Documentation
    description: CMiC's Power BI Connector allows users to connect Microsoft Power BI directly to CMiC ERP data through the CMiC API, enabling business intelligence dashboards and reports for construction project financials, job costing, and operational metrics.
    x-features:
      - name: Power BI Native
        description: Native Power BI connector for CMiC ERP data.
      - name: Pre-Modeled Datasets
        description: Pre-modeled construction-financial datasets out of the box.
    x-useCases:
      - name: Executive Dashboards
        description: Build executive dashboards on CMiC project and financial data.
      - name: Job Profitability Analysis
        description: Analyze profitability across jobs, cost codes, and projects.
common:
  - url: https://cmicglobal.com/
    type: Website
  - url: openapi/cmic-construction-erp-openapi.yml
    type: OpenAPI
  - url: json-schema/cmic-project-schema.json
    type: JSONSchema
  - url: json-ld/cmic-context.jsonld
    type: JSONLDContext
  - url: rules/cmic-rules.yml
    type: SpectralRuleset
  - url: capabilities/cmic-construction-erp-capabilities.yml
    type: NaftikoCapabilities
  - url: https://developers.cmicglobal.com/
    type: Portal
  - url: https://docs.cmicglobal.com/portal/Content/Home.htm
    type: Documentation
  - url: https://developers.cmicglobal.com/v1/docs/authentication
    type: Authentication
  - url: https://developers.cmicglobal.com/docs/developer-api-account
    type: GettingStarted
  - url: https://cmicglobal.com/integrations/api-bundles/
    type: Integrations
  - url: https://cmicglobal.com/privacy-policy
    type: PrivacyPolicy
  - url: https://cmicglobal.com/resources/
    type: Blog
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
