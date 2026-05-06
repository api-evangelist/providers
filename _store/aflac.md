---
aid: aflac
url: https://raw.githubusercontent.com/api-evangelist/aflac/refs/heads/main/apis.yml
modified: '2026-04-19'
apis:
  - aid: aflac:enterprise-connect-api
    name: Aflac Enterprise Connect API
    tags:
      - Benefits
      - Enrollment
      - Insurance
      - Supplemental Insurance
      - Workforce
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.enterprise-connect.aflac.com
    humanURL: https://docs.enterprise-connect.aflac.com
    properties:
      - url: https://docs.enterprise-connect.aflac.com
        type: Documentation
      - url: https://docs.enterprise-connect.aflac.com/docs/getting-started
        type: GettingStarted
      - type: OpenAPI
        url: openapi/aflac-enterprise-connect-openapi.yml
    description: The Aflac Enterprise Connect (AEC) API enables benefits administrators, HR platforms, and third-party enrollment systems to integrate with Aflac's supplemental insurance platform programmatically. It provides REST API access to benefits enrollment, policy management, claims status, and eligibility verification for group and individual supplemental insurance products. The API supports electronic benefits enrollment workflows replacing traditional EDI 834 file exchanges, enabling real-time enrollment confirmation and policy administration for employers and their benefits technology partners.
  - aid: aflac:claims-api
    name: Aflac Claims API
    tags:
      - Claims
      - Insurance
      - Payments
      - Supplemental Insurance
    image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
    baseURL: https://api.enterprise-connect.aflac.com
    humanURL: https://docs.enterprise-connect.aflac.com
    properties:
      - url: https://docs.enterprise-connect.aflac.com
        type: Documentation
    description: The Aflac Claims API provides programmatic access to supplemental insurance claim submission, status retrieval, and benefit payment tracking. It enables policyholders and administrators to submit claims digitally, track claim processing status, and receive benefit payment notifications. The API supports claims for Aflac's portfolio of supplemental products including accident, critical illness, cancer, hospital indemnity, and short-term disability insurance.
common:
  - type: Portal
    url: https://docs.enterprise-connect.aflac.com
  - type: Website
    url: https://www.aflac.com
  - type: SignUp
    url: https://www.aflac.com/business/default.aspx
  - type: TermsOfService
    url: https://www.aflac.com/about-aflac/legal/terms-and-conditions.aspx
  - type: PrivacyPolicy
    url: https://www.aflac.com/about-aflac/legal/privacy-policy.aspx
  - type: Support
    url: https://www.aflac.com/contact-aflac/default.aspx
  - type: Features
    data:
      - name: Electronic Benefits Enrollment
        description: Replace EDI 834 file-based enrollment with real-time API-driven enrollment workflows for supplemental insurance products.
      - name: Policy Administration
        description: Manage group and individual supplemental insurance policies including enrollments, terminations, and coverage changes.
      - name: Claims Submission
        description: Enable digital claim filing for supplemental insurance products including accident, critical illness, cancer, and disability coverage.
      - name: Eligibility Verification
        description: Verify employee eligibility for Aflac supplemental insurance products in real time during enrollment.
      - name: Benefits Administration Integration
        description: Connect benefits administration platforms with Aflac's enrollment and policy systems via standardized REST APIs.
      - name: Real-Time Enrollment Confirmation
        description: Receive immediate enrollment confirmation and policy numbers upon successful enrollment submission.
  - type: UseCases
    data:
      - name: HR Platform Integration
        description: HR and benefits administration platforms integrate with Aflac's API to offer supplemental insurance enrollment within their existing benefits workflows.
      - name: Employer Self-Service Enrollment
        description: Employers manage supplemental insurance enrollments for employees during open enrollment periods via connected benefits platforms.
      - name: Claims Tracking
        description: Employees and HR teams track the status of Aflac supplemental insurance claims submitted after a qualifying health event.
      - name: Benefits Broker Workflow
        description: Benefits brokers manage group policy setup, employee enrollment, and plan changes for employer clients through integrated tools.
  - type: Integrations
    data:
      - name: Employee Navigator
        description: Aflac connects with Employee Navigator benefits administration platform for automated enrollment data exchange.
      - name: Benefitfocus
        description: Integration with Benefitfocus benefits marketplace for supplemental insurance enrollment.
      - name: ADP
        description: Payroll and HR integration with ADP for Aflac premium deduction and enrollment synchronization.
      - name: Workday
        description: Enterprise HR platform integration for benefits enrollment and Aflac policy administration.
      - name: bswift
        description: Benefits administration platform integration for Aflac group enrollment.
  - type: OpenAPI
    url: openapi/aflac-enterprise-connect-openapi.yml
  - type: JSONSchema
    url: json-schema/enterprise-connect-claim-list-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-claim-request-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-claim-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-dependent-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-eligibility-request-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-eligibility-response-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-enrollment-list-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-enrollment-request-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-enrollment-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-group-list-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-group-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-policy-list-schema.json
  - type: JSONSchema
    url: json-schema/enterprise-connect-policy-schema.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-claim-list-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-claim-request-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-claim-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-dependent-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-eligibility-request-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-eligibility-response-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-enrollment-list-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-enrollment-request-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-enrollment-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-group-list-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-group-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-policy-list-structure.json
  - type: JSONStructure
    url: json-structure/enterprise-connect-policy-structure.json
  - type: JSON-LD
    url: json-ld/aflac-enterprise-context.jsonld
  - type: Example
    url: examples/enterprise-connect-claim-example.json
  - type: Example
    url: examples/enterprise-connect-claim-list-example.json
  - type: Example
    url: examples/enterprise-connect-claim-request-example.json
  - type: Example
    url: examples/enterprise-connect-dependent-example.json
  - type: Example
    url: examples/enterprise-connect-eligibility-request-example.json
  - type: Example
    url: examples/enterprise-connect-eligibility-response-example.json
  - type: Example
    url: examples/enterprise-connect-enrollment-example.json
  - type: Example
    url: examples/enterprise-connect-enrollment-list-example.json
  - type: Example
    url: examples/enterprise-connect-enrollment-request-example.json
  - type: Example
    url: examples/enterprise-connect-group-example.json
  - type: Example
    url: examples/enterprise-connect-group-list-example.json
  - type: Example
    url: examples/enterprise-connect-policy-example.json
  - type: Example
    url: examples/enterprise-connect-policy-list-example.json
  - type: SpectralRules
    url: rules/aflac-spectral-rules.yml
  - type: Vocabulary
    url: vocabulary/aflac-vocabulary.yaml
  - type: NaftikoCapability
    url: capabilities/benefits-administration.yaml
description: Aflac is America's leading provider of supplemental insurance, offering products that pay benefits when a policyholder experiences an accident, illness, or injury. Aflac provides REST APIs through its Enterprise Connect (AEC) platform enabling benefits technology companies, HR platforms, and benefits administrators to integrate supplemental insurance enrollment, policy management, and claims capabilities into their workflows.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
