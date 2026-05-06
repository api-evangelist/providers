---
aid: adobe-captivate
url: https://raw.githubusercontent.com/api-evangelist/adobe-captivate/refs/heads/main/apis.yml
name: Adobe Captivate
description: Adobe Captivate is an eLearning authoring tool used to create responsive eLearning content, software demonstrations, and interactive training modules.
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
type: Index
created: '2024-01-20'
modified: '2026-04-19'
specificationVersion: '0.19'
tags:
  - Authoring
  - Education
  - eLearning
  - LMS
  - SCORM
  - Training
  - xAPI
apis:
  - name: Adobe Captivate Prime API
    description: Learning Management System API for managing courses, learners, and learning content.
    image: https://www.adobe.com/content/dam/cc/icons/captivate-prime.svg
    humanURL: https://www.adobe.com/products/captivateprime.html
    baseURL: https://learningmanager.adobe.com/primeapi/v2
    tags:
      - Courses
      - Learners
      - Learning Management
      - LMS
    properties:
      - type: Documentation
        url: https://captivateprime.adobe.com/docs/primeapi/v2/
      - type: OpenAPI
        url: https://learningmanager.adobe.com/primeapi/v2/swagger.json
      - type: OpenAPI
        url: openapi/adobe-captivate-prime-api-openapi.yml
      - type: Authentication
        url: https://captivateprime.adobe.com/docs/primeapi/v2/#authentication
      - type: Postman Collection
        url: https://www.postman.com/adobe-captivate-prime
      - type: JSONSchema
        url: json-schema/prime-api-account-response-schema.json
      - type: JSONSchema
        url: json-schema/prime-api-account-schema.json
      - type: JSONSchema
        url: json-schema/prime-api-badge-list-response-schema.json
      - type: JSONStructure
        url: json-structure/prime-api-account-response-structure.json
      - type: JSONStructure
        url: json-structure/prime-api-account-structure.json
      - type: JSONStructure
        url: json-structure/prime-api-badge-list-response-structure.json
  - name: Adobe Captivate SCORM API
    description: API for SCORM-compliant content delivery and tracking.
    humanURL: https://helpx.adobe.com/captivate/using/publish-projects-scorm-compliant-lms.html
    tags:
      - Content Delivery
      - LMS Integration
      - SCORM
    properties:
      - type: Documentation
        url: https://scorm.com/scorm-explained/technical-scorm/
      - type: Specification
        url: https://adlnet.gov/projects/scorm/
  - name: Adobe Captivate xAPI (Tin Can API)
    description: Experience API for tracking learning experiences.
    humanURL: https://helpx.adobe.com/captivate/using/xapi-tin-can-support.html
    tags:
      - Learning Analytics
      - Tin Can
      - xAPI
    properties:
      - type: Documentation
        url: https://xapi.com/overview/
      - type: Specification
        url: https://github.com/adlnet/xAPI-Spec
  - name: Adobe Captivate Review API
    description: API for collaborative review and commenting on eLearning projects.
    humanURL: https://helpx.adobe.com/captivate/using/shared-review.html
    tags:
      - Collaboration
      - Comments
      - Review
    properties:
      - type: Documentation
        url: https://helpx.adobe.com/captivate/using/shared-review.html
  - name: Adobe Learning Manager Webhooks API
    description: Webhooks API for Adobe Learning Manager that enables real-time event notifications for learner activities, course completions, enrollments, and other learning management events.
    humanURL: https://experienceleague.adobe.com/docs/learning-manager/using/integration/feature-summary/webhooks.html
    tags:
      - Events
      - Learning Management
      - Notifications
      - Webhooks
    properties:
      - type: Documentation
        url: https://experienceleague.adobe.com/docs/learning-manager/using/integration/feature-summary/webhooks.html
      - type: AsyncAPI
        url: asyncapi/adobe-captivate-learning-manager-webhooks-asyncapi.yml
      - type: JSONSchema
        url: json-schema/learning-manager-webhooks-badge-awarded-payload-schema.json
      - type: JSONSchema
        url: json-schema/learning-manager-webhooks-certification-completed-payload-schema.json
      - type: JSONSchema
        url: json-schema/learning-manager-webhooks-course-created-payload-schema.json
      - type: JSONStructure
        url: json-structure/learning-manager-webhooks-badge-awarded-payload-structure.json
      - type: JSONStructure
        url: json-structure/learning-manager-webhooks-certification-completed-payload-structure.json
      - type: JSONStructure
        url: json-structure/learning-manager-webhooks-course-created-payload-structure.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
common:
  - type: Support
    url: https://helpx.adobe.com/support/captivate.html
  - type: Community
    url: https://community.adobe.com/t5/adobe-captivate/ct-p/ct-captivate
  - type: Blog
    url: https://elearning.adobe.com/
  - type: StatusPage
    url: https://status.adobe.com/
  - type: TermsOfService
    url: https://www.adobe.com/legal/terms.html
  - type: PrivacyPolicy
    url: https://www.adobe.com/privacy.html
  - type: Contact
    url: https://www.adobe.com/products/captivate/contact.html
  - type: Portal
    url: https://experienceleague.adobe.com/docs/learning-manager/using/introduction.html
  - type: GettingStarted
    url: https://experienceleague.adobe.com/docs/learning-manager/using/getting-started/getting-started.html
  - type: Documentation
    url: https://experienceleague.adobe.com/docs/learning-manager/using/home.html
  - type: Console
    url: https://developer.adobe.com/console/
  - type: ChangeLog
    url: https://experienceleague.adobe.com/docs/learning-manager/using/whats-new.html
  - type: Website
    url: https://business.adobe.com/products/learning-manager/adobe-learning-manager.html
  - type: Login
    url: https://learningmanager.adobe.com/
  - type: YouTube
    url: https://www.youtube.com/user/AdobeELearning
  - type: GitHubOrganization
    url: https://github.com/adobe
  - type: JSONSchema
    url: json-schema/adobe-captivate-learning-object-schema.json
  - type: JSON-LD
    url: json-ld/adobe-captivate-context.jsonld
  - type: Features
    data:
      - name: Learning Object Management
        description: Create and manage courses, learning programs, certifications, and job aids with full CRUD operations via REST API.
      - name: Learner Enrollment and Tracking
        description: Programmatically enroll learners, track progress, and retrieve completion status across all learning objects.
      - name: Webhook Event Notifications
        description: Receive real-time HTTP POST notifications for enrollment, completion, badge, and certification events.
      - name: Gamification and Badges
        description: Manage gamification points, leaderboards, and badge awards to motivate learners.
      - name: Catalog Management
        description: Organize and expose learning content through catalogs with filtering and tagging capabilities.
      - name: Skill Tracking
        description: Associate skills with learning content and track learner skill attainment through the API.
      - name: OAuth 2.0 Authentication
        description: Secure API access using OAuth 2.0 with role-based scopes for admin, learner, manager, and author roles.
      - name: SCORM and xAPI Support
        description: Deliver and track SCORM-compliant and xAPI (Tin Can) learning content for LMS interoperability.
      - name: Bulk Data Import/Export
        description: Use the Jobs API to import and export users, enrollments, and completion data in bulk.
      - name: Notification Management
        description: Manage announcements and notifications sent to learners, managers, and administrators.
  - type: UseCases
    data:
      - name: HR System Integration
        description: Automatically provision users from HRIS systems like Workday or SAP SuccessFactors into Adobe Learning Manager.
      - name: Custom Learning Portal
        description: Build branded training portals that surface Adobe Learning Manager content through the REST API.
      - name: Compliance Training Automation
        description: Auto-enroll new hires in mandatory compliance courses and track completion for regulatory reporting.
      - name: Learning Analytics Dashboard
        description: Extract learner progress and completion data to build custom analytics and reporting dashboards.
      - name: E-Commerce Integration
        description: Integrate course purchases with e-commerce platforms and auto-enroll paying customers.
      - name: Real-Time Progress Monitoring
        description: Use webhooks to monitor learner activity in real time and trigger downstream workflows on completion.
      - name: Certification Management
        description: Automate certification enrollment, renewal reminders, and expiry tracking using the REST API.
  - type: Integrations
    data:
      - name: Salesforce
        description: Sync learner data and completion status between Adobe Learning Manager and Salesforce CRM.
      - name: Microsoft Teams
        description: Surface learning content and notifications directly within Microsoft Teams via connector.
      - name: Workday
        description: Import organizational user data from Workday HCM to manage learner accounts automatically.
      - name: SAP SuccessFactors
        description: Bi-directional sync with SAP SuccessFactors for user provisioning and learning record exchange.
      - name: Adobe Experience Manager
        description: Embed learning content and catalogs within Adobe Experience Manager sites.
      - name: Zoom
        description: Schedule and launch virtual classroom sessions directly from Adobe Learning Manager.
      - name: LinkedIn Learning
        description: Import LinkedIn Learning content into Adobe Learning Manager catalogs for blended learning.
      - name: SCORM Cloud
        description: Host and launch SCORM content packages through SCORM Cloud integration.
  - type: SpectralRules
    url: rules/adobe-captivate-spectral-rules.yml
  - type: NaftikoCapability
    url: capabilities/learning-management.yaml
  - type: Vocabulary
    url: vocabulary/adobe-captivate-vocabulary.yaml
  - type: JSON-LD
    url: json-ld/adobe-captivate-learning-manager-webhooks-context.jsonld
  - type: JSON-LD
    url: json-ld/adobe-captivate-prime-api-context.jsonld
---
