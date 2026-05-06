---
name: Microsoft Access
description: Microsoft Access is a database management system from Microsoft that combines the relational Microsoft Jet Database Engine with a graphical user interface and software development tools.
image: https://www.microsoft.com/en-us/microsoft-365/access
tags:
  - Access Database
  - Database
  - Desktop Database
  - Microsoft
  - Relational Database
created: '2024'
modified: '2026-04-28'
url: https://www.microsoft.com/en-us/microsoft-365/access
specificationVersion: '0.18'
apis:
  - name: Microsoft Access Database Engine API
    description: API for programmatic access to Microsoft Access databases through various interfaces including ODBC, OLE DB, and DAO.
    image: https://www.microsoft.com/en-us/microsoft-365/access
    humanUrl: https://learn.microsoft.com/en-us/office/client-developer/access/access-home
    baseUrl: https://api.example.com/access
    tags:
      - DAO
      - Database
      - ODBC
      - OLE DB
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/
      - type: OpenAPI
        url: https://example.com/openapi.json
      - type: Tutorials
        url: https://learn.microsoft.com/en-us/office/vba/access/concepts/miscellaneous/concepts-access-vba-reference
  - name: Microsoft Graph API (for Access Online)
    description: API for accessing Microsoft Access databases stored in SharePoint or OneDrive through Microsoft Graph.
    image: https://learn.microsoft.com/graph/images/microsoft-graph.png
    humanUrl: https://learn.microsoft.com/en-us/graph/overview
    baseUrl: https://graph.microsoft.com/v1.0
    tags:
      - Cloud Database
      - Microsoft Graph
      - SharePoint
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/graph/api/resources/list
      - type: Authentication
        url: https://learn.microsoft.com/en-us/graph/auth/
      - type: SDKs
        url: https://learn.microsoft.com/en-us/graph/sdks/sdks-overview
  - name: Microsoft Access VBA API
    description: The Access Visual Basic for Applications (VBA) object model provides programmatic access to all Access objects, properties, methods, and events for developing custom solutions and automating database operations.
    image: https://www.microsoft.com/en-us/microsoft-365/access
    humanUrl: https://learn.microsoft.com/en-us/office/vba/api/overview/access
    tags:
      - Automation
      - Macros
      - Object Model
      - VBA
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/vba/api/overview/access
      - type: Object Model Reference
        url: https://learn.microsoft.com/en-us/office/vba/api/overview/access/object-model
      - type: Application Object Reference
        url: https://learn.microsoft.com/en-us/office/vba/api/access.application
      - type: DoCmd Object Reference
        url: https://learn.microsoft.com/en-us/office/vba/api/access.docmd
  - name: Microsoft Data Access Objects (DAO) API
    description: Data Access Objects (DAO) provide a programmatic interface to create, query, and modify the structure and data of Access databases, with objects like Database, Recordset, TableDef, QueryDef, and more mapping directly to database constructs.
    image: https://www.microsoft.com/en-us/microsoft-365/access
    humanUrl: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/microsoft-data-access-objects-reference
    tags:
      - DAO
      - Data Access
      - QueryDef
      - Recordset
      - TableDef
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/microsoft-data-access-objects-reference
      - type: Database Object Reference
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/database-object-dao
  - name: Microsoft ActiveX Data Objects (ADO) API
    description: ActiveX Data Objects (ADO) enable client applications to access and manipulate data from Access databases through OLE DB providers, supporting features for building client/server and web-based applications with extensions for multidimensional data (ADO MD) and schema management (ADOX).
    image: https://www.microsoft.com/en-us/microsoft-365/access
    humanUrl: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/microsoft-activex-data-objects-reference
    tags:
      - ActiveX
      - ADO
      - Data Access
      - OLE DB
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/microsoft-activex-data-objects-reference
      - type: OLE DB Providers Reference
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/ole-db-providers
  - name: Microsoft Access SQL API
    description: The Microsoft Access SQL reference provides documentation for the Access SQL dialect, including data definition language (DDL) for creating and modifying database structures and data manipulation language (DML) for querying and updating data.
    image: https://www.microsoft.com/en-us/microsoft-365/access
    humanUrl: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/microsoft-access-sql-reference
    tags:
      - DDL
      - DML
      - Query
      - SQL
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/microsoft-access-sql-reference
      - type: SQL Reference Overview
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/overview-of-the-access-sql-reference
  - name: Microsoft Access Macro Actions API
    description: The Access macro actions interface provides a set of programmable actions for automating database tasks including data operations, form management, navigation, filtering, and system commands without writing VBA code.
    image: https://www.microsoft.com/en-us/microsoft-365/access
    humanUrl: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/access-macro-actions-access-developer-reference
    tags:
      - Actions
      - Automation
      - Macros
      - No-Code
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/access-macro-actions-access-developer-reference
      - type: Macro Commands Reference
        url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/macro-commands
  - name: Power Automate Access Actions API
    description: Power Automate for desktop provides built-in actions for automating Microsoft Access databases, including launching Access instances, reading tables, running stored queries, executing macros, and closing databases programmatically within desktop flows.
    image: https://www.microsoft.com/en-us/microsoft-365/access
    humanUrl: https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access
    tags:
      - Automation
      - Desktop Flows
      - Power Automate
      - RPA
    properties:
      - type: Documentation
        url: https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/access
common:
  - type: Portal
    url: https://www.microsoft.com/en-us/microsoft-365
  - type: Support
    url: https://support.microsoft.com/access
  - type: Pricing
    url: https://www.microsoft.com/en-us/microsoft-365/access/compare-microsoft-access-plans-and-pricing
  - type: Blog
    url: https://techcommunity.microsoft.com/t5/access-blog/bg-p/AccessBlog
  - type: Terms of Service
    url: https://www.microsoft.com/en-us/servicesagreement
  - type: Developer Documentation
    url: https://learn.microsoft.com/en-us/office/client-developer/access/access-home
  - type: Desktop Database Reference
    url: https://learn.microsoft.com/en-us/office/client-developer/access/desktop-database-reference/
  - type: Access Database Engine Download
    url: https://www.microsoft.com/en-us/download/details.aspx?id=54920
  - type: Privacy Policy
    url: https://privacy.microsoft.com/en-us/privacystatement
  - type: JSON-LD
    url: json-ld/microsoft-access-context.jsonld
  - type: JSONSchema
    url: json-schema/microsoft-access-database-schema.json
  - type: JSONSchema
    url: json-schema/microsoft-access-table-schema.json
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
    url: https://apievangelist.com
---
