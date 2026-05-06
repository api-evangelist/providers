---
aid: moodle
specificationVersion: '0.19'
name: Moodle
description: Moodle is the world's open source learning platform, used by educators and organizations to deliver online courses and learning experiences. The Moodle developer platform exposes a broad set of internal APIs for plugin and core development, plus a Web Services API that enables external systems to integrate with Moodle for users, courses, enrollments, grading, and more.
type: Index
position: Consuming
access: 3rd-Party
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
url: https://raw.githubusercontent.com/api-evangelist/moodle/refs/heads/main/apis.yml
created: '2025-01-08'
modified: '2026-04-28'
tags:
  - E-Learning
  - EdTech
  - LMS
  - Moodle
  - Open Source
  - Web Services
apis:
  - aid: moodle:web-services
    name: Moodle Web Services API
    description: Exposes Moodle functionality as web services so external programs can integrate with a Moodle site for users, courses, enrollments, grading, and other operations. Supports REST, XML-RPC, and SOAP protocols with token-based authentication.
    humanURL: https://moodledev.io/docs/apis/subsystems/external/
    tags:
      - External
      - Integration
      - REST
      - SOAP
      - Web Services
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/external/
  - aid: moodle:external-functions
    name: Moodle External Functions API
    description: Allows developers to expose parametrized functions to external systems, forming the basis of Moodle's web services and powering integrations consumed via REST, SOAP, and XML-RPC.
    humanURL: https://moodledev.io/docs/apis/subsystems/external/functions
    tags:
      - External
      - Functions
      - Integration
      - Web Services
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/external/functions
  - aid: moodle:access
    name: Moodle Access API
    description: Provides functions to determine what the current user is allowed to do, checking roles, capabilities, and permissions across system, course, and activity contexts.
    humanURL: https://moodledev.io/docs/apis/subsystems/access
    tags:
      - Access
      - Authorization
      - Permissions
      - Roles
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/access
  - aid: moodle:roles
    name: Moodle Roles API
    description: An extension of the Access API that defines the set of actions a user is allowed to perform on certain system levels through assignable roles and capabilities.
    humanURL: https://moodledev.io/docs/apis/subsystems/access/roles
    tags:
      - Access
      - Capabilities
      - Permissions
      - Roles
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/access/roles
  - aid: moodle:dml
    name: Moodle Data Manipulation API (DML)
    description: Enables safe, consistent database read and write operations across Moodle, abstracting the underlying database driver and providing helpers for common query patterns.
    humanURL: https://moodledev.io/docs/apis/core/dml
    tags:
      - Database
      - DML
      - Persistence
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/core/dml
  - aid: moodle:file
    name: Moodle File API
    description: Manages file storage across plugins, providing a unified interface for uploading, retrieving, and serving files associated with users, courses, and activities.
    humanURL: https://moodledev.io/docs/apis/subsystems/files
    tags:
      - Files
      - Storage
      - Uploads
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/files
  - aid: moodle:form
    name: Moodle Form API
    description: Defines and processes user data submitted through web forms, including validation, rendering, and persistence.
    humanURL: https://moodledev.io/docs/apis/subsystems/form
    tags:
      - Forms
      - UI
      - Validation
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/form
  - aid: moodle:events
    name: Moodle Events API
    description: Defines event handlers for inter-plugin communication and logging, enabling decoupled, observer-style integrations across Moodle.
    humanURL: https://moodledev.io/docs/apis/core/event
    tags:
      - Events
      - Logging
      - Observers
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/core/event
  - aid: moodle:hooks
    name: Moodle Hooks API
    description: Enables indirect communication between core and plugins through well-defined extension points, allowing plugins to react to and modify core behavior.
    humanURL: https://moodledev.io/docs/apis/core/hooks
    tags:
      - Extensibility
      - Hooks
      - Plugins
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/core/hooks
  - aid: moodle:privacy
    name: Moodle Privacy API
    description: Describes stored personal data and supports discovery, export, and deletion of user data across plugins for GDPR and similar privacy compliance.
    humanURL: https://moodledev.io/docs/apis/subsystems/privacy
    tags:
      - Compliance
      - GDPR
      - Privacy
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/privacy
  - aid: moodle:task
    name: Moodle Task API
    description: Executes background jobs on a schedule or as one-off operations, allowing plugins to defer long-running work to cron processing.
    humanURL: https://moodledev.io/docs/apis/subsystems/task
    tags:
      - Background Jobs
      - Cron
      - Scheduling
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/task
  - aid: moodle:payment
    name: Moodle Payment API
    description: Manages payment processing in Moodle, providing pluggable payment gateways for paid enrollments and other monetized features.
    humanURL: https://moodledev.io/docs/apis/subsystems/payment
    tags:
      - Enrollment
      - Gateways
      - Payments
    properties:
      - type: Documentation
        url: https://moodledev.io/docs/apis/subsystems/payment
common:
  - type: Portal
    url: https://moodledev.io
  - type: Documentation
    url: https://moodledev.io/docs/apis
  - type: Website
    url: https://moodle.org
  - type: Blog
    url: https://moodle.com/news/
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
