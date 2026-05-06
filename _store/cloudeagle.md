---
aid: cloudeagle
name: CloudEagle.ai
url: https://raw.githubusercontent.com/api-evangelist/cloudeagle/refs/heads/main/apis.yml
created: '2026-03-16'
modified: '2026-04-27'
specificationVersion: '0.19'
type: Index
access: 3rd-Party
position: Consumer
x-type: company
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Access Governance
  - Cost Optimization
  - License Management
  - Procurement
  - SaaS Management
  - Shadow AI
  - Shadow IT
  - Software Procurement
  - Vendor Management
description: CloudEagle.ai is an AI-powered SaaS management and procurement platform that helps IT, security, finance, and procurement teams discover, govern, optimize, and renew their SaaS and AI application portfolio. The platform offers application discovery via 500+ direct integrations with SSO, HRIS, finance, and CASB systems; license harvesting and spend optimization; identity and access governance with automated access reviews; onboarding/offboarding automation; SaaS procurement and renewal orchestration; and shadow IT/shadow AI detection. CloudEagle exposes an enterprise API to programmatically access these capabilities for partners and customers; specific endpoint paths and authentication details are provided to customers via the in-product developer settings rather than a public docs site.
apis:
  - aid: cloudeagle:cloudeagle-api
    name: CloudEagle API
    tags:
      - Access Governance
      - License Management
      - SaaS Management
      - Software Procurement
      - Vendor Management
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    humanURL: https://www.cloudeagle.ai/
    properties:
      - url: https://www.cloudeagle.ai/blogs/enterprise-api-and-saas-management
        type: Reference
      - url: https://www.cloudeagle.ai/integrations
        type: Integrations
      - url: https://www.cloudeagle.ai/
        type: Documentation
    description: 'The CloudEagle API is an enterprise REST surface that exposes the same SaaS-management primitives as the web app: discovered applications, licenses and usage, identity and access state, onboarding/offboarding workflows, vendor and contract records, and procurement workflows. CloudEagle does not publish a fully open developer portal; access to API specifications and credentials is provisioned to customer tenants and partners via account-level settings, and integration documentation is shared directly with onboarded customers.'
common:
  - type: Website
    url: https://www.cloudeagle.ai/
  - type: Integrations
    url: https://www.cloudeagle.ai/integrations
  - type: Resources
    url: https://www.cloudeagle.ai/resources/guides-and-reports
  - type: SaaSManagement
    url: https://www.cloudeagle.ai/product/saas-management
  - type: PrivacyPolicy
    url: https://www.cloudeagle.ai/privacy-policy
  - type: Naftiko Capabilities
    url: capabilities/cloudeagle-capabilities.yml
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
