---
access_model:
  confidence: high
  label: Paid · Self-serve signup
  onboarding: self-serve
  pricing: paid
  public: false
  source:
  - plans
  - authentication
  trial: false
  try_now: false
agent_readiness:
  band: agent-ready
  band_gated_from: agent-native
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: derived
    agentic_commerce: false
    auth_clarity: served
    consent_identity: false
    delegated_identity: served
    dry_run_mode: false
    dynamic_client_registration: true
    error_semantics: verified
    event_surface_described: true
    idempotency: false
    mcp_server: verified
    openapi_examples: partial
    protected_resource_metadata: verified
    rate_limit_signal: verified
    reversibility_documented: documented
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 65.0
  scored_at: '2026-10-03'
agentic_access:
- acting_count: 59
  human_in_the_loop: 0
  name: Adobe Agentic Access
  operation_count: 96
  slug: adobe-agentic-access
  summary_line: 96 operations · 59 acting
api_count: 4
apis:
- description: Extract text, images, tables, and more from native and scanned PDFs into structured JSON using AI technology.
  name: Adobe PDF Extract API
  slug: adobe-pdf-extract-api
- description: Embed e-signature workflows and manage signing agreements programmatically.
  name: Adobe Acrobat Sign API
  slug: adobe-acrobat-sign-api
- description: Access and analyze digital marketing data and metrics.
  name: Adobe Analytics API
  slug: adobe-analytics-api
- description: Generate and edit images using generative AI models through a RESTful API.
  name: Adobe Firefly API
  slug: adobe-firefly-api
- description: Build and manage customer experience applications on Adobe Experience Platform.
  name: Adobe Experience Platform API
  slug: adobe-experience-platform-api
- description: Search, license, and manage Adobe Stock assets including photos, vectors, videos, and templates.
  name: Adobe Stock API
  slug: adobe-stock-api
- description: Build and integrate e-commerce applications with REST, GraphQL, and SOAP web APIs.
  name: Adobe Commerce API
  slug: adobe-commerce-api
- description: Automate marketing processes and manage leads, campaigns, and assets via REST APIs.
  name: Adobe Marketo Engage API
  slug: adobe-marketo-engage-api
- description: Manage work, projects, tasks, and resources programmatically with a REST API.
  name: Adobe Workfront API
  slug: adobe-workfront-api
- description: Programmatically manage users, groups, and product entitlements for Adobe enterprise organizations.
  name: Adobe User Management API
  slug: adobe-user-management-api
- description: Subscribe to and receive near real-time events from Adobe services for event-driven integrations.
  name: Adobe I/O Events API
  slug: adobe-io-events-api
- description: Create, read, update, and delete content, assets, and forms in Adobe Experience Manager as a Cloud Service.
  name: Adobe Experience Manager API
  slug: adobe-experience-manager-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Automatically add accessibility tags to PDF documents using AI.
  name: Adobe PDF Services Accessibility Auto-Tag API
  phrasing_intents:
  - id: autoTagPDF
    intent: Auto-tag an uploaded PDF for accessibility
    question: How do I make an uploaded PDF meet WCAG 2.0 and PDF/UA with automatic tags?
  phrasing_ops: 1
  slug: adobe-accessibility-auto-tag-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Upload and manage assets (source files) for PDF operations.
  name: Adobe PDF Services Assets API
  phrasing_intents:
  - id: asset.uploadpresignedurl
    intent: Get an upload URL for a new asset
    question: How do I upload a PDF so PDF Services operations can use it?
  - id: asset.get
    intent: Get a download URL for an asset
    question: Where can I download the content of an asset I stored?
  - id: asset.delete
    intent: Delete an asset from storage
    question: Can I remove a stored asset from the cloud provider before it expires?
  - id: asset.metadata
    intent: Get the metadata of a stored asset
    question: What metadata is kept for a temporary asset I uploaded?
  - id: getAsset
    intent: Get a download URI for an asset or job output
    question: How do I download the result file from a finished PDF job?
  - id: deleteAsset
    intent: Delete a previously uploaded asset
    question: Can I delete an asset I uploaded to the platform by its asset ID?
  phrasing_ops: 6
  slug: adobe-assets-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Combine multiple PDF documents into a single PDF.
  name: Adobe PDF Services Combine PDF API
  phrasing_intents:
  - id: pdfoperations.combinepdf
    intent: Merge several PDFs into one
    question: How do I merge several PDF files into a single document?
  - id: pdfoperations.combinepdf.jobstatus
    intent: Check the status of a PDF merge job
    question: Is my PDF merge job finished yet?
  phrasing_ops: 2
  slug: adobe-combine-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Reduce the file size of PDF documents while maintaining quality.
  name: Adobe PDF Services Compress PDF API
  phrasing_intents:
  - id: pdfoperations.compresspdf
    intent: Shrink the file size of a PDF
    question: Can I reduce the file size of a large PDF before emailing it?
  - id: pdfoperations.compresspdf.jobstatus
    intent: Check the status of a PDF compression job
    question: Has my PDF compression job completed?
  phrasing_ops: 2
  slug: adobe-compress-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Create PDF documents from supported file formats including Microsoft Office, images, and HTML.
  name: Adobe PDF Services Create PDF API
  phrasing_intents:
  - id: pdfoperations.createpdf
    intent: Convert Office, Markdown or image files to PDF
    question: How do I turn a Word, Excel or PowerPoint file into a PDF?
  - id: pdfoperations.jobstatus
    intent: Check the status of a create-PDF job
    question: Is my Office-to-PDF conversion done?
  phrasing_ops: 2
  slug: adobe-create-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Delete specific pages from a PDF document.
  name: Adobe PDF Services Delete Pages API
  phrasing_intents:
  - id: deletePages
    intent: Remove pages from a PDF
    question: How do I remove specific pages from a PDF?
  phrasing_ops: 1
  slug: adobe-delete-pages-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Generate PDF and Word documents from templates with dynamic JSON data.
  name: Adobe PDF Services Document Generation API
  phrasing_intents:
  - id: pdfoperations.documentgeneration
    intent: Generate documents from a Word template and JSON
    question: How do I fill a Word template with JSON data to produce contracts or invoices?
  - id: pdfoperations.documentgeneration.jobstatus
    intent: Check the status of a document generation job
    question: Is my templated document ready yet?
  phrasing_ops: 2
  slug: adobe-document-generation-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Export (convert) PDF documents to other formats such as DOCX, PPTX, XLSX, images, and RTF.
  name: Adobe PDF Services Export PDF API
  phrasing_intents:
  - id: pdfoperations.exportpdf
    intent: Export a PDF to Word, Excel, PowerPoint or RTF
    question: Can I convert a PDF back into an editable Word document?
  - id: pdfoperations.exportpdf.jobstatus
    intent: Check the status of a PDF export job
    question: Has my PDF to Word export finished?
  phrasing_ops: 2
  slug: adobe-export-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Extract text, tables, and figures from PDF documents into structured JSON output.
  name: Adobe PDF Services Extract PDF API
  phrasing_intents:
  - id: pdfoperations.extractpdf
    intent: Extract text, tables and figures from a PDF as JSON
    question: How do I extract structured text with headings and paragraphs from a PDF?
  - id: pdfoperations.extractpdf.jobstatus
    intent: Check the status of a PDF extraction job
    question: Has my PDF content extraction finished?
  phrasing_ops: 2
  slug: adobe-extract-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Insert pages from one PDF into another.
  name: Adobe PDF Services Insert Pages API
  phrasing_intents:
  - id: insertPages
    intent: Insert pages from other PDFs into a PDF
    question: How do I insert pages from one PDF into another at a specific position?
  phrasing_ops: 1
  slug: adobe-insert-pages-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Poll for the status and results of asynchronous PDF operations.
  name: Adobe PDF Services Jobs API
  phrasing_intents:
  - id: getJobStatus
    intent: Check the status of any PDF operation job
    question: How do I poll whether an asynchronous PDF job is in progress, done or failed?
  phrasing_ops: 1
  slug: adobe-jobs-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Optimize PDFs for fast web viewing (linearization).
  name: Adobe PDF Services Linearize PDF API
  phrasing_intents:
  - id: pdfoperations.linearizepdf
    intent: Make a PDF web-optimized (linearized)
    question: How do I make a PDF load page by page in a browser?
  - id: pdfoperations.linearizepdf.jobstatus
    intent: Check the status of a linearize job
    question: Is my web-optimized PDF done?
  phrasing_ops: 2
  slug: adobe-linearize-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Apply optical character recognition to scanned PDFs to make text searchable and selectable.
  name: Adobe PDF Services OCR API
  phrasing_intents:
  - id: pdfoperations.ocr
    intent: Make a scanned PDF searchable with OCR
    question: How do I make text in a scanned PDF searchable?
  - id: pdfoperations.ocr.jobstatus
    intent: Check the status of an OCR job
    question: Has my OCR job finished?
  phrasing_ops: 2
  slug: adobe-ocr-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Retrieve metadata and properties from PDF documents.
  name: Adobe PDF Services PDF Properties API
  phrasing_intents:
  - id: pdfoperations.pdfproperties
    intent: Get a PDF's page count, version and properties
    question: How many pages does this PDF have and what PDF version is it?
  - id: pdfoperations.pdfproperties.jobstatus
    intent: Check the status of a PDF properties job
    question: Is the PDF properties lookup finished?
  phrasing_ops: 2
  slug: adobe-pdf-properties-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Add password protection and encryption to PDF documents.
  name: Adobe PDF Services Protect PDF API
  phrasing_intents:
  - id: pdfoperations.protectpdf
    intent: Password-protect a PDF and restrict permissions
    question: How do I password-protect a PDF?
  - id: pdfoperations.protectpdf.jobstatus
    intent: Check the status of a PDF protection job
    question: Is my password-protected PDF ready?
  phrasing_ops: 2
  slug: adobe-protect-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Remove password protection from PDF documents.
  name: Adobe PDF Services Remove Protection API
  phrasing_intents:
  - id: pdfoperations.removeprotection
    intent: Remove password protection from a PDF
    question: How do I remove the password from a PDF I own?
  - id: pdfoperations.removeprotection.jobstatus
    intent: Check the status of a remove-protection job
    question: Is my unlocked PDF ready?
  phrasing_ops: 2
  slug: adobe-remove-protection-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Reorder pages within a PDF document.
  name: Adobe PDF Services Reorder Pages API
  phrasing_intents:
  - id: reorderPages
    intent: Reorder the pages of a PDF
    question: How do I rearrange the order of pages in a PDF?
  phrasing_ops: 1
  slug: adobe-reorder-pages-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Replace pages in a PDF with pages from another PDF.
  name: Adobe PDF Services Replace Pages API
  phrasing_intents:
  - id: replacePages
    intent: Replace pages in a PDF with pages from another
    question: How do I swap out certain pages of a PDF with pages from another PDF?
  phrasing_ops: 1
  slug: adobe-replace-pages-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Rotate pages within a PDF document.
  name: Adobe PDF Services Rotate Pages API
  phrasing_intents:
  - id: rotatePages
    intent: Rotate pages in a PDF
    question: How do I rotate specific pages of a PDF?
  phrasing_ops: 1
  slug: adobe-rotate-pages-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Split a PDF document into multiple smaller PDFs.
  name: Adobe PDF Services Split PDF API
  phrasing_intents:
  - id: pdfoperations.splitpdf
    intent: Split a PDF into several smaller PDFs
    question: How do I split a large PDF into smaller files?
  - id: pdfoperations.splitpdf.jobstatus
    intent: Check the status of a PDF split job
    question: Is my PDF split finished?
  phrasing_ops: 2
  slug: adobe-split-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The Composites API from Adobe — 1 operation(s) for composites.
  name: Adobe Composites API
  phrasing_intents:
  - id: v1/composites/compose
    intent: Generate a composite image around a 3D object
    question: How do I place a 3D product into an AI-generated scene from a text prompt?
  phrasing_ops: 1
  slug: adobe-composites-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The Export PDF Form Data API will retrieve the data from a PDF form and return it as a JSON file.
  name: Adobe Export PDF Form Data API
  phrasing_intents:
  - id: pdfoperations.getformdata
    intent: Read the filled-in data from a PDF form
    question: How do I pull the values someone typed into a PDF form as JSON?
  - id: pdfoperations.getformdata.jobstatus
    intent: Check the status of a form data export job
    question: Is the JSON from my PDF form export ready?
  phrasing_ops: 2
  slug: adobe-export-pdf-form-data-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: 'Creates an access token using client id and client secret. Click <a href="https://developer.adobe.com/developer-console/docs/guides/authentication/ServerToServerAuthentication/IMS/">here</a> to refer '
  name: Adobe Generate Token API
  phrasing_intents:
  - id: authentication.generatetoken
    intent: Get an access token for PDF Services
    question: How do I get an access token to call PDF Services?
  phrasing_ops: 1
  slug: adobe-generate-token-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Convert HTML Resources to a PDF File
  name: Adobe Html to PDF API
  phrasing_intents:
  - id: pdfoperations.htmltopdf
    intent: Convert HTML or a web page URL to PDF
    question: How do I turn a web page URL into a PDF?
  - id: pdfoperations.htmltopdf.jobstatus
    intent: Check the status of an HTML-to-PDF job
    question: Is my HTML to PDF conversion done?
  phrasing_ops: 2
  slug: adobe-html-to-pdf-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The Import PDF Form Data API will take the form data provided as a JSON, insert it into the PDF form, and generate the resulting PDF.
  name: Adobe Import PDF Form Data API
  phrasing_intents:
  - id: pdfoperations.setformdata
    intent: Fill a PDF form from JSON data
    question: Can I fill in a PDF form automatically from JSON?
  - id: pdfoperations.setformdata.jobstatus
    intent: Check the status of a form fill job
    question: Is my filled-in PDF form ready?
  phrasing_ops: 2
  slug: adobe-import-pdf-form-data-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: App-facing APIs for Adobe CC Libraries.
  name: Adobe Library Service API
  phrasing_intents:
  - id: getLibraries
    intent: List my Creative Cloud libraries
    question: Which Creative Cloud Libraries do I have access to?
  - id: createLibraries
    intent: Create a new Creative Cloud library
    question: How do I create a new Creative Cloud library through the API?
  - id: getLibrary
    intent: Get the details of one library
    question: What details can I pull for a single library by its ID?
  - id: headLibrary
    intent: Check that a library exists
    question: How can I check whether a library still exists without downloading its contents?
  - id: deleteLibrary
    intent: Delete a library
    question: Can I permanently remove a whole Creative Cloud library?
  - id: patchLibrary
    intent: Run a batch of changes on one library
    question: Can I apply several changes to a library in a single serial batch request?
  - id: unArchiveLibraryElements
    intent: Restore archived library elements
    question: Can I bring back library elements I moved to the archive?
  - id: deleteLibraryElements
    intent: Permanently delete archived elements
    question: How do I permanently purge several archived elements from a library at once?
  phrasing_ops: 19
  slug: adobe-library-service-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: App-facing APIs specifically for Adobe CC Library Bookmarks.
  name: Adobe Library Service - Bookmarks API
  phrasing_intents:
  - id: getBookmarks
    intent: List my library bookmarks
    question: Which libraries have I bookmarked?
  - id: addLibraryBookmarks
    intent: Bookmark one or more libraries
    question: How do I bookmark a library so I can find it again?
  - id: putLibraryBookmark
    intent: Update an existing bookmark
    question: Can I change a bookmark I already saved?
  - id: removeLibraryBookmark
    intent: Remove a library bookmark
    question: How do I remove a library from my bookmarks?
  phrasing_ops: 4
  slug: adobe-library-service-bookmarks-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: App-facing APIs specifically for Adobe CC Public Libraries.
  name: Adobe Library Service - Public API
  phrasing_intents:
  - id: getPublicLibrary
    intent: Get a publicly shared library
    question: Can I read a library someone shared publicly with a link?
  - id: headPublicLibrary
    intent: Check that a public library exists
    question: How can I check that a shared public library link still works?
  - id: getPublicLibraryElements
    intent: List elements of a public library
    question: What elements are in a library that was shared publicly?
  - id: getPublicLibraryElement
    intent: Get one element from a public library
    question: Can I fetch a single element from a publicly shared library?
  phrasing_ops: 4
  slug: adobe-library-service-public-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Rotate and delete pages of a PDF File
  name: Adobe Page Manipulation API
  phrasing_intents:
  - id: pdfoperations.pagemanipulation
    intent: Rotate and delete pages in one PDF job
    question: Can I rotate some pages and delete others in a PDF in one request?
  - id: pdfoperations.pagemanipulation.jobstatus
    intent: Check the status of a page manipulation job
    question: Is my combined rotate-and-delete page job done?
  phrasing_ops: 2
  slug: adobe-page-manipulation-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Operation to create the tagged pdf and excel report for accessibility auto-tag use case.
  name: Adobe PDF Accessibility Auto-Tag API
  phrasing_intents:
  - id: pdfoperations.autotag
    intent: Auto-tag a PDF for accessibility
    question: How do I add accessibility tags to an untagged PDF automatically?
  - id: pdfoperations.autotag.jobstatus
    intent: Check the status of an auto-tag job
    question: Is my accessibility auto-tagging finished?
  phrasing_ops: 2
  slug: adobe-pdf-accessibility-auto-tag-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Accessibility Checker API will check PDF files to see if they meet the machine-verifiable requirements of PDF/UA and WCAG.
  name: Adobe PDF Accessibility Checker API
  phrasing_intents:
  - id: pdfoperations.accessibilitychecker
    intent: Check a PDF against PDF/UA and WCAG
    question: Does my PDF meet PDF/UA and WCAG accessibility requirements?
  - id: pdfoperations.accessibilitychecker.jobstatus
    intent: Check the status of an accessibility check job
    question: Is my accessibility check report ready?
  phrasing_ops: 2
  slug: adobe-pdf-accessibility-checker-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Create electronic seal on PDF documents like invoices, agreements etc using the digital certificate issued to the user by Trust Service Provider.
  name: Adobe PDF Electronic Seal API
  phrasing_intents:
  - id: pdfoperations.electronicseal
    intent: Apply an electronic seal to a PDF
    question: How do I apply an organization's electronic seal to a PDF?
  - id: pdfoperations.electronicseal.jobstatus
    intent: Check the status of an electronic seal job
    question: Has my PDF sealing job finished?
  phrasing_ops: 2
  slug: adobe-pdf-electronic-seal-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Convert a PDF File to image files
  name: Adobe PDF To Images API
  phrasing_intents:
  - id: pdfoperations.pdftoimages
    intent: Convert PDF pages to images
    question: How do I turn every page of a PDF into an image?
  - id: pdfoperations.pdftoimages.jobstatus
    intent: Check the status of a PDF-to-images job
    question: Are my page images ready?
  phrasing_ops: 2
  slug: adobe-pdf-to-images-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: Extract content from PDF documents and output it in a well-formatted LLM-friendly Markdown text, along with tables and figures
  name: Adobe PDF To Markdown API
  phrasing_intents:
  - id: pdfoperations.pdftomarkdown
    intent: Convert a PDF into Markdown
    question: Can I convert a PDF into Markdown for an LLM pipeline?
  - id: pdfoperations.pdftomarkdown.jobstatus
    intent: Check the status of a PDF-to-Markdown job
    question: Is my Markdown conversion finished?
  phrasing_ops: 2
  slug: adobe-pdf-to-markdown-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: PDF Watermark API will add a watermark in PDF document.
  name: Adobe PDF Watermark API
  phrasing_intents:
  - id: pdfoperations.addwatermark
    intent: Add a watermark to a PDF
    question: How do I stamp a watermark onto pages of a PDF?
  - id: pdfoperations.addwatermark.jobstatus
    intent: Check the status of a watermark job
    question: Is my watermarked PDF ready?
  phrasing_ops: 2
  slug: adobe-pdf-watermark-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The Scenes API from Adobe — 5 operation(s) for scenes.
  name: Adobe Scenes API
  phrasing_intents:
  - id: v1/scenes/assemble
    intent: Assemble a 3D scene from source files
    question: How do I assemble several 3D models into one scene with Substance 3D?
  - id: v1/scenes/convert
    intent: Convert a 3D file to another format
    question: Can I convert an FBX model into a different 3D format?
  - id: v1/scenes/describe
    intent: Describe the contents of a 3D scene
    question: What is inside a 3D scene file, such as its meshes, materials and cameras?
  - id: v1/scenes/render
    intent: Render a 3D object to an image
    question: How do I render a product image from a 3D model with a ground plane and auto framing?
  - id: v1/scenes/render-basic
    intent: Render a 3D object with the basic renderer
    question: Is there a basic, lighter version of the 3D render call?
  phrasing_ops: 5
  slug: adobe-scenes-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The Spaces API from Adobe — 2 operation(s) for spaces.
  name: Adobe Spaces API
  phrasing_intents:
  - id: createSpace_v1
    intent: Create a Space from 3D files (v1)
    question: How do I upload 3D files into a Space with the original v1 endpoint?
  - id: createSpace_v2
    intent: Upload files to a new Space (v2)
    question: Can I upload a whole folder tree of textures and models into a v2 space?
  phrasing_ops: 2
  slug: adobe-spaces-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The SpacesFrameIO API from Adobe — 1 operation(s) for spacesframeio.
  name: Adobe Spaces Frame IO API
  phrasing_intents:
  - id: createSpaceFromFrameIO_v2
    intent: Create a Space from a frame.io folder
    question: Can I pull a folder from frame.io into a Substance 3D space?
  phrasing_ops: 1
  slug: adobe-spacesframeio-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The SpacesNextFrameIO API from Adobe — 1 operation(s) for spacesnextframeio.
  name: Adobe Spaces Next Frame IO API
  phrasing_intents:
  - id: createSpaceFromNextFrameIO_v2
    intent: Create a Space from a next.frame.io folder
    question: Can I create a space from a folder on next.frame.io?
  phrasing_ops: 1
  slug: adobe-spacesnextframeio-api
- baseURL: https://pdf-services.adobe.io
  baseurl_source: declared
  description: The SpacesURL API from Adobe — 1 operation(s) for spacesurl.
  name: Adobe Spaces URL API
  phrasing_intents:
  - id: createSpaceURL_v2
    intent: Create a Space from files at URLs
    question: Can I build a Substance 3D space from files hosted at public URLs?
  phrasing_ops: 1
  slug: adobe-spacesurl-api
arazzos:
- description: Upload a PDF, auto-tag it for accessibility, poll the job, and fetch the tagged result.
  name: Adobe Auto-tag a PDF For Accessibility
  slug: adobe-auto-tag-pdf-workflow
- description: Upload two PDFs, combine them into a single document, poll the job, and fetch the merged result.
  name: Adobe Combine Two PDFs Into One
  slug: adobe-combine-pdfs-workflow
- description: Upload a PDF, compress it to reduce file size, poll the job, and fetch the smaller result.
  name: Adobe Compress a PDF
  slug: adobe-compress-pdf-workflow
- description: Upload a source document, convert it to PDF, poll the async job, and fetch the download URI.
  name: Adobe Create PDF From Source File
  slug: adobe-create-pdf-workflow
- description: Upload a PDF, delete a page range, poll the job, and fetch the trimmed result.
  name: Adobe Delete Pages From a PDF
  slug: adobe-delete-pages-workflow
- description: Resolve a download URI for a finished output asset, then delete it from the platform.
  name: Adobe Download Then Clean Up an Asset
  slug: adobe-download-and-cleanup-asset-workflow
- description: Upload a PDF, export it to DOCX/PPTX/XLSX/RTF/image, poll the job, and fetch the result.
  name: Adobe Export PDF To Another Format
  slug: adobe-export-pdf-workflow
- description: Upload a PDF, extract text and tables into structured JSON, poll the job, and fetch the result.
  name: Adobe Extract Content From a PDF
  slug: adobe-extract-pdf-workflow
- description: Upload a Word template, merge JSON data into it, poll the job, and fetch the generated document.
  name: Adobe Generate a Document From a Template
  slug: adobe-generate-document-workflow
- description: Upload a PDF, request its metadata properties, and poll the job until done or failed.
  name: Adobe Inspect PDF Properties
  slug: adobe-inspect-pdf-properties-workflow
- description: Upload a scanned PDF, run OCR to make it searchable, poll the job, and fetch the result.
  name: Adobe OCR a Scanned PDF
  slug: adobe-ocr-pdf-workflow
- description: Upload a PDF, apply password protection and encryption, poll the job, and fetch the result.
  name: Adobe Protect a PDF With a Password
  slug: adobe-protect-pdf-workflow
- description: Upload a protected PDF, unlock it with its password, poll the job, and fetch the result.
  name: Adobe Remove Protection From a PDF
  slug: adobe-remove-protection-workflow
- description: Upload a PDF, rotate a page range, poll the job, and fetch the rotated result.
  name: Adobe Rotate Pages In a PDF
  slug: adobe-rotate-pages-workflow
- description: Upload a PDF, split it by page count into multiple files, poll the job, and fetch the result.
  name: Adobe Split a PDF
  slug: adobe-split-pdf-workflow
artifact_total: 256
asyncapis:
- description: ''
  name: Adobe Pdf Services Webhooks
  slug: adobe-pdf-services-webhooks
collections:
- collection_type: postman
  name: Adobe PDF Services API
  slug: postman-adobe-pdf-services-api
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Adobe PDF Services Accessibility Auto-Tag API
  slug: open-adobe-accessibility-auto-tag-api
- collection_type: open
  name: Adobe PDF Services Assets API
  slug: open-adobe-assets-api
- collection_type: open
  name: Adobe PDF Services Combine PDF API
  slug: open-adobe-combine-pdf-api
- collection_type: open
  name: Adobe PDF Services Compress PDF API
  slug: open-adobe-compress-pdf-api
- collection_type: open
  name: Adobe PDF Services Create PDF API
  slug: open-adobe-create-pdf-api
- collection_type: open
  name: Adobe PDF Services Delete Pages API
  slug: open-adobe-delete-pages-api
- collection_type: open
  name: Adobe PDF Services Document Generation API
  slug: open-adobe-document-generation-api
- collection_type: open
  name: Adobe PDF Services Export PDF API
  slug: open-adobe-export-pdf-api
- collection_type: open
  name: Adobe PDF Services Extract PDF API
  slug: open-adobe-extract-pdf-api
- collection_type: open
  name: Adobe PDF Services Insert Pages API
  slug: open-adobe-insert-pages-api
- collection_type: open
  name: Adobe PDF Services Jobs API
  slug: open-adobe-jobs-api
- collection_type: open
  name: Adobe PDF Services Linearize PDF API
  slug: open-adobe-linearize-pdf-api
- collection_type: open
  name: Adobe PDF Services OCR API
  slug: open-adobe-ocr-api
- collection_type: open
  name: Adobe PDF Services PDF Properties API
  slug: open-adobe-pdf-properties-api
- collection_type: open
  name: Adobe PDF Services API
  slug: open-adobe-pdf-services-api
- collection_type: open
  name: Adobe PDF Services Protect PDF API
  slug: open-adobe-protect-pdf-api
- collection_type: open
  name: Adobe PDF Services Remove Protection API
  slug: open-adobe-remove-protection-api
- collection_type: open
  name: Adobe PDF Services Reorder Pages API
  slug: open-adobe-reorder-pages-api
- collection_type: open
  name: Adobe PDF Services Replace Pages API
  slug: open-adobe-replace-pages-api
- collection_type: open
  name: Adobe PDF Services Rotate Pages API
  slug: open-adobe-rotate-pages-api
- collection_type: open
  name: Adobe PDF Services Split PDF API
  slug: open-adobe-split-pdf-api
common:
- group: company
  title: ''
  type: Website
  url: https://www.adobe.com/
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/packages/adobe-packages.yml
  title: ''
  type: Packages
  url: packages/adobe-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/packages/adobe-packages.yml
  title: ''
  type: SDKs
  url: packages/adobe-packages.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/well-known/adobe-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/adobe-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/well-known/adobe-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/adobe-security.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/llms/adobe-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/adobe-llms.txt
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/mcp/adobe-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/adobe-mcp.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/mcp/adobe-tool-crosswalk.yml
  title: ''
  type: ToolCrosswalk
  url: mcp/adobe-tool-crosswalk.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/conformance/adobe-conformance.yml
  title: ''
  type: Conformance
  url: conformance/adobe-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.adobe.com/trust/compliance/compliance-list.html
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/security/adobe-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/adobe-trust-center.yml
- group: auth
  title: ''
  type: Security
  url: https://helpx.adobe.com/security.html/security/policy.ug.html
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/errors/adobe-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/adobe-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/lifecycle/adobe-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/adobe-lifecycle.yml
- group: operate
  title: ''
  type: Deprecation
  url: https://developer.adobe.com/document-services/docs/overview/pdf-services-api/policies/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/conventions/adobe-conventions.yml
  title: ''
  type: Conventions
  url: conventions/adobe-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/data-model/adobe-data-model.yml
  title: ''
  type: DataModel
  url: data-model/adobe-data-model.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/overlays/adobe-pdf-services-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/adobe-pdf-services-overlay.yaml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/asyncapi/adobe-pdf-services-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/adobe-pdf-services-webhooks.yml
- group: start
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/sandbox/adobe-sandbox.yml
  title: ''
  type: Sandbox
  url: sandbox/adobe-sandbox.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/changelog/adobe-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/adobe-changelog.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/cli/adobe-cli.yml
  title: ''
  type: CLI
  url: cli/adobe-cli.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/components/adobe-components.yml
  title: ''
  type: Components
  url: components/adobe-components.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/plans/adobe-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/adobe-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/rate-limits/adobe-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/adobe-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/finops/adobe-finops.yml
  title: ''
  type: FinOps
  url: finops/adobe-finops.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/openapi/_original/adobe-pdf-services-api-openapi-official.json
  title: ''
  type: OpenAPI
  url: openapi/_original/adobe-pdf-services-api-openapi-official.json
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/openapi/_original/adobe-substance-3d-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/adobe-substance-3d-api-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/openapi/_original/adobe-cc-libraries-api-openapi.json
  title: ''
  type: OpenAPI
  url: openapi/_original/adobe-cc-libraries-api-openapi.json
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/agentic-access/adobe-agentic-access.yml
  title: ''
  type: AgenticAccess
  url: agentic-access/adobe-agentic-access.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/security/adobe-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/adobe-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/security/adobe-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/adobe-domain-security.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/authentication/adobe-authentication.yml
  title: ''
  type: Authentication
  url: authentication/adobe-authentication.yml
- group: build
  title: ''
  type: PostmanWorkspace
  url: https://www.postman.com/kinlaneapi/adobe/overview
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-auto-tag-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-auto-tag-pdf-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-combine-pdfs-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-combine-pdfs-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-compress-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-compress-pdf-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-create-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-create-pdf-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-delete-pages-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-delete-pages-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-download-and-cleanup-asset-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-download-and-cleanup-asset-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-export-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-export-pdf-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-extract-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-extract-pdf-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-generate-document-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-generate-document-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-inspect-pdf-properties-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-inspect-pdf-properties-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-ocr-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-ocr-pdf-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-protect-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-protect-pdf-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-remove-protection-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-remove-protection-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-rotate-pages-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-rotate-pages-workflow.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/arazzo/adobe-split-pdf-workflow.yml
  title: ''
  type: Arazzo
  url: arazzo/adobe-split-pdf-workflow.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/adobe
- group: start
  title: ''
  type: Portal
  url: https://developer.adobe.com/
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.adobe.com/
- group: docs
  title: ''
  type: Documentation
  url: https://developer.adobe.com/apis/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.adobe.com/document-services/docs/apis/
- group: commercial
  title: ''
  type: Pricing
  url: https://developer.adobe.com/document-services/pricing/main/
- group: build
  title: ''
  type: Postman
  url: https://www.postman.com/kinlaneapi/adobe/overview
- group: start
  title: ''
  type: Console
  url: https://developer.adobe.com/console/
- group: auth
  title: ''
  type: Authentication
  url: https://developer.adobe.com/developer-console/docs/guides/authentication/
- group: operate
  title: ''
  type: Support
  url: https://developer.adobe.com/developer-support/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.adobe.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.developer.adobe.com/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.adobe.com/legal/terms.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.adobe.com/privacy/policy.html
- group: start
  title: ''
  type: GettingStarted
  url: https://developer.adobe.com/developer-console/docs/guides/getting-started
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/AdobeDocs/
- group: build
  title: ''
  type: SDKs
  url: https://developer.adobe.com/apis
- group: start
  title: ''
  type: Signup
  url: https://developer.adobe.com/console/
- group: start
  title: ''
  type: Login
  url: https://developer.adobe.com/console/
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/openapi/_original/adobe-pdf-services-api-openapi.yml
  title: ''
  type: OpenAPI
  url: openapi/_original/adobe-pdf-services-api-openapi.yml
- group: docs
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/json-schema/adobe-pdf-services-asset-upload-request-schema.json
  title: ''
  type: JSONSchema
  url: json-schema/adobe-pdf-services-asset-upload-request-schema.json
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/json-ld/adobe-context.jsonld
  title: ''
  type: JSONLD
  url: json-ld/adobe-context.jsonld
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/rules/adobe-spectral-rules.yml
  title: ''
  type: SpectralRules
  url: rules/adobe-spectral-rules.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/vocabulary/adobe-vocabulary.yaml
  title: ''
  type: Vocabulary
  url: vocabulary/adobe-vocabulary.yaml
- group: agent
  title: ''
  type: MCPServer
  url: https://developer.adobe.com/express/add-ons/docs/guides/getting-started/local-development/mcp-server
- group: operate
  title: ''
  type: RateLimits
  url: https://developer.adobe.com/document-services/docs/overview/limits/
- group: operate
  title: ''
  type: ChangeLog
  url: https://developer.adobe.com/firefly-services/docs/firefly-api/
created: '2024-01-01'
description: Adobe provides APIs and developer resources for its creative, document, and experience cloud platforms. Developers can integrate with PDF services, Creative Cloud, generative AI (Firefly), analytics, e-commerce, e-signatures, and many other Adobe products and services.
examples:
- key_count: 6
  name: Adobe Autotagpdf Example
  slug: adobe-autotagpdf-example
- key_count: 6
  name: Adobe Combinepdf Example
  slug: adobe-combinepdf-example
- key_count: 6
  name: Adobe Compresspdf Example
  slug: adobe-compresspdf-example
- key_count: 6
  name: Adobe Createpdf Example
  slug: adobe-createpdf-example
- key_count: 6
  name: Adobe Deletepages Example
  slug: adobe-deletepages-example
- key_count: 6
  name: Adobe Exportpdf Example
  slug: adobe-exportpdf-example
- key_count: 6
  name: Adobe Extractpdf Example
  slug: adobe-extractpdf-example
- key_count: 6
  name: Adobe Generatedocument Example
  slug: adobe-generatedocument-example
- key_count: 6
  name: Adobe Getasset Example
  slug: adobe-getasset-example
- key_count: 6
  name: Adobe Getjobstatus Example
  slug: adobe-getjobstatus-example
- key_count: 6
  name: Adobe Getpdfproperties Example
  slug: adobe-getpdfproperties-example
- key_count: 6
  name: Adobe Insertpages Example
  slug: adobe-insertpages-example
- key_count: 6
  name: Adobe Linearizepdf Example
  slug: adobe-linearizepdf-example
- key_count: 6
  name: Adobe Ocrpdf Example
  slug: adobe-ocrpdf-example
- key_count: 2
  name: Adobe Pdf Services Asset Download Response Example
  slug: adobe-pdf-services-asset-download-response-example
- key_count: 1
  name: Adobe Pdf Services Asset Reference Example
  slug: adobe-pdf-services-asset-reference-example
- key_count: 1
  name: Adobe Pdf Services Asset Upload Request Example
  slug: adobe-pdf-services-asset-upload-request-example
- key_count: 2
  name: Adobe Pdf Services Asset Upload Response Example
  slug: adobe-pdf-services-asset-upload-response-example
- key_count: 3
  name: Adobe Pdf Services Auto Tag Request Example
  slug: adobe-pdf-services-auto-tag-request-example
- key_count: 1
  name: Adobe Pdf Services Combine Pdf Request Example
  slug: adobe-pdf-services-combine-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Compress Pdf Request Example
  slug: adobe-pdf-services-compress-pdf-request-example
- key_count: 6
  name: Adobe Pdf Services Create Pdf Request Example
  slug: adobe-pdf-services-create-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Delete Pages Request Example
  slug: adobe-pdf-services-delete-pages-request-example
- key_count: 4
  name: Adobe Pdf Services Document Generation Request Example
  slug: adobe-pdf-services-document-generation-request-example
- key_count: 1
  name: Adobe Pdf Services Error Response Example
  slug: adobe-pdf-services-error-response-example
- key_count: 3
  name: Adobe Pdf Services Export Pdf Request Example
  slug: adobe-pdf-services-export-pdf-request-example
- key_count: 6
  name: Adobe Pdf Services Extract Pdf Request Example
  slug: adobe-pdf-services-extract-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Insert Pages Request Example
  slug: adobe-pdf-services-insert-pages-request-example
- key_count: 3
  name: Adobe Pdf Services Job Status Response Example
  slug: adobe-pdf-services-job-status-response-example
- key_count: 1
  name: Adobe Pdf Services Linearize Pdf Request Example
  slug: adobe-pdf-services-linearize-pdf-request-example
- key_count: 3
  name: Adobe Pdf Services Ocr Request Example
  slug: adobe-pdf-services-ocr-request-example
- key_count: 2
  name: Adobe Pdf Services Page Range Example
  slug: adobe-pdf-services-page-range-example
- key_count: 2
  name: Adobe Pdf Services Pdf Properties Request Example
  slug: adobe-pdf-services-pdf-properties-request-example
- key_count: 4
  name: Adobe Pdf Services Protect Pdf Request Example
  slug: adobe-pdf-services-protect-pdf-request-example
- key_count: 2
  name: Adobe Pdf Services Remove Protection Request Example
  slug: adobe-pdf-services-remove-protection-request-example
- key_count: 2
  name: Adobe Pdf Services Reorder Pages Request Example
  slug: adobe-pdf-services-reorder-pages-request-example
- key_count: 2
  name: Adobe Pdf Services Replace Pages Request Example
  slug: adobe-pdf-services-replace-pages-request-example
- key_count: 2
  name: Adobe Pdf Services Rotate Pages Request Example
  slug: adobe-pdf-services-rotate-pages-request-example
- key_count: 2
  name: Adobe Pdf Services Split Pdf Request Example
  slug: adobe-pdf-services-split-pdf-request-example
- key_count: 6
  name: Adobe Protectpdf Example
  slug: adobe-protectpdf-example
- key_count: 6
  name: Adobe Removeprotection Example
  slug: adobe-removeprotection-example
- key_count: 6
  name: Adobe Reorderpages Example
  slug: adobe-reorderpages-example
- key_count: 6
  name: Adobe Replacepages Example
  slug: adobe-replacepages-example
- key_count: 6
  name: Adobe Rotatepages Example
  slug: adobe-rotatepages-example
- key_count: 6
  name: Adobe Splitpdf Example
  slug: adobe-splitpdf-example
- key_count: 6
  name: Adobe Uploadasset Example
  slug: adobe-uploadasset-example
features:
- PDF creation, conversion, and manipulation via REST API
- AI-powered PDF content extraction into structured JSON
- Generative AI image creation and editing with Firefly
- E-signature workflows with Acrobat Sign
- Digital analytics and marketing insights
- Customer data platform with Experience Platform
- Content management with Experience Manager
- Marketing automation with Marketo Engage
- E-commerce platform with Adobe Commerce
- Work management and project tracking with Workfront
- Event-driven integrations with I/O Events
- Stock asset search and licensing
finops:
- name: Adobe Finops
  service_category: Creative + Marketing + Document SaaS
  slug: adobe-finops
image: /assets/icons/adobe.png
integrations:
- Microsoft 365 and Teams integration
- Salesforce CRM integration
- Adobe Creative Cloud libraries
- Workfront and Jira project management
- SAP and Oracle ERP systems
- Shopify and Magento marketplaces
- Google Analytics and Tag Manager
- Slack and Microsoft Teams notifications
json_schemas:
- name: AssetDownloadResponse
  property_count: 2
  slug: adobe-assetdownloadresponse
- name: AssetReference
  property_count: 1
  slug: adobe-assetreference
- name: AssetUploadRequest
  property_count: 1
  slug: adobe-assetuploadrequest
- name: AssetUploadResponse
  property_count: 2
  slug: adobe-assetuploadresponse
- name: AutoTagRequest
  property_count: 3
  slug: adobe-autotagrequest
- name: CombinePDFRequest
  property_count: 1
  slug: adobe-combinepdfrequest
- name: CompressPDFRequest
  property_count: 2
  slug: adobe-compresspdfrequest
- name: CreatePDFRequest
  property_count: 6
  slug: adobe-createpdfrequest
- name: DeletePagesRequest
  property_count: 2
  slug: adobe-deletepagesrequest
- name: DocumentGenerationRequest
  property_count: 4
  slug: adobe-documentgenerationrequest
- name: ErrorResponse
  property_count: 1
  slug: adobe-errorresponse
- name: ExportPDFRequest
  property_count: 3
  slug: adobe-exportpdfrequest
- name: ExtractPDFRequest
  property_count: 6
  slug: adobe-extractpdfrequest
- name: InsertPagesRequest
  property_count: 2
  slug: adobe-insertpagesrequest
- name: JobStatusResponse
  property_count: 3
  slug: adobe-jobstatusresponse
- name: LinearizePDFRequest
  property_count: 1
  slug: adobe-linearizepdfrequest
- name: OCRRequest
  property_count: 3
  slug: adobe-ocrrequest
- name: PageRange
  property_count: 2
  slug: adobe-pagerange
- name: Adobe PDF Services Job
  property_count: 3
  slug: adobe-pdf-job
- name: AssetDownloadResponse
  property_count: 2
  slug: adobe-pdf-services-asset-download-response
- name: AssetReference
  property_count: 1
  slug: adobe-pdf-services-asset-reference
- name: AssetUploadRequest
  property_count: 1
  slug: adobe-pdf-services-asset-upload-request
- name: AssetUploadResponse
  property_count: 2
  slug: adobe-pdf-services-asset-upload-response
- name: AutoTagRequest
  property_count: 3
  slug: adobe-pdf-services-auto-tag-request
- name: CombinePDFRequest
  property_count: 1
  slug: adobe-pdf-services-combine-pdf-request
- name: CompressPDFRequest
  property_count: 2
  slug: adobe-pdf-services-compress-pdf-request
- name: CreatePDFRequest
  property_count: 6
  slug: adobe-pdf-services-create-pdf-request
- name: DeletePagesRequest
  property_count: 2
  slug: adobe-pdf-services-delete-pages-request
- name: DocumentGenerationRequest
  property_count: 4
  slug: adobe-pdf-services-document-generation-request
- name: ErrorResponse
  property_count: 1
  slug: adobe-pdf-services-error-response
- name: ExportPDFRequest
  property_count: 3
  slug: adobe-pdf-services-export-pdf-request
- name: ExtractPDFRequest
  property_count: 6
  slug: adobe-pdf-services-extract-pdf-request
- name: InsertPagesRequest
  property_count: 2
  slug: adobe-pdf-services-insert-pages-request
- name: JobStatusResponse
  property_count: 3
  slug: adobe-pdf-services-job-status-response
- name: LinearizePDFRequest
  property_count: 1
  slug: adobe-pdf-services-linearize-pdf-request
- name: OCRRequest
  property_count: 3
  slug: adobe-pdf-services-ocr-request
- name: PageRange
  property_count: 2
  slug: adobe-pdf-services-page-range
- name: PDFPropertiesRequest
  property_count: 2
  slug: adobe-pdf-services-pdf-properties-request
- name: ProtectPDFRequest
  property_count: 4
  slug: adobe-pdf-services-protect-pdf-request
- name: RemoveProtectionRequest
  property_count: 2
  slug: adobe-pdf-services-remove-protection-request
- name: ReorderPagesRequest
  property_count: 2
  slug: adobe-pdf-services-reorder-pages-request
- name: ReplacePagesRequest
  property_count: 2
  slug: adobe-pdf-services-replace-pages-request
- name: RotatePagesRequest
  property_count: 2
  slug: adobe-pdf-services-rotate-pages-request
- name: SplitPDFRequest
  property_count: 2
  slug: adobe-pdf-services-split-pdf-request
- name: PDFPropertiesRequest
  property_count: 2
  slug: adobe-pdfpropertiesrequest
- name: ProtectPDFRequest
  property_count: 4
  slug: adobe-protectpdfrequest
- name: RemoveProtectionRequest
  property_count: 2
  slug: adobe-removeprotectionrequest
- name: ReorderPagesRequest
  property_count: 2
  slug: adobe-reorderpagesrequest
- name: ReplacePagesRequest
  property_count: 2
  slug: adobe-replacepagesrequest
- name: RotatePagesRequest
  property_count: 2
  slug: adobe-rotatepagesrequest
- name: SplitPDFRequest
  property_count: 2
  slug: adobe-splitpdfrequest
json_structures:
- name: Adobe Pdf Services Asset Download Response Structure
  property_count: 2
  slug: adobe-pdf-services-asset-download-response-structure
- name: Adobe Pdf Services Asset Reference Structure
  property_count: 1
  slug: adobe-pdf-services-asset-reference-structure
- name: Adobe Pdf Services Asset Upload Request Structure
  property_count: 1
  slug: adobe-pdf-services-asset-upload-request-structure
- name: Adobe Pdf Services Asset Upload Response Structure
  property_count: 2
  slug: adobe-pdf-services-asset-upload-response-structure
- name: Adobe Pdf Services Auto Tag Request Structure
  property_count: 3
  slug: adobe-pdf-services-auto-tag-request-structure
- name: Adobe Pdf Services Combine Pdf Request Structure
  property_count: 1
  slug: adobe-pdf-services-combine-pdf-request-structure
- name: Adobe Pdf Services Compress Pdf Request Structure
  property_count: 2
  slug: adobe-pdf-services-compress-pdf-request-structure
- name: Adobe Pdf Services Create Pdf Request Structure
  property_count: 6
  slug: adobe-pdf-services-create-pdf-request-structure
- name: Adobe Pdf Services Delete Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-delete-pages-request-structure
- name: Adobe Pdf Services Document Generation Request Structure
  property_count: 4
  slug: adobe-pdf-services-document-generation-request-structure
- name: Adobe Pdf Services Error Response Structure
  property_count: 1
  slug: adobe-pdf-services-error-response-structure
- name: Adobe Pdf Services Export Pdf Request Structure
  property_count: 3
  slug: adobe-pdf-services-export-pdf-request-structure
- name: Adobe Pdf Services Extract Pdf Request Structure
  property_count: 6
  slug: adobe-pdf-services-extract-pdf-request-structure
- name: Adobe Pdf Services Insert Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-insert-pages-request-structure
- name: Adobe Pdf Services Job Status Response Structure
  property_count: 3
  slug: adobe-pdf-services-job-status-response-structure
- name: Adobe Pdf Services Linearize Pdf Request Structure
  property_count: 1
  slug: adobe-pdf-services-linearize-pdf-request-structure
- name: Adobe Pdf Services Ocr Request Structure
  property_count: 3
  slug: adobe-pdf-services-ocr-request-structure
- name: Adobe Pdf Services Page Range Structure
  property_count: 2
  slug: adobe-pdf-services-page-range-structure
- name: Adobe Pdf Services Pdf Properties Request Structure
  property_count: 2
  slug: adobe-pdf-services-pdf-properties-request-structure
- name: Adobe Pdf Services Protect Pdf Request Structure
  property_count: 4
  slug: adobe-pdf-services-protect-pdf-request-structure
- name: Adobe Pdf Services Remove Protection Request Structure
  property_count: 2
  slug: adobe-pdf-services-remove-protection-request-structure
- name: Adobe Pdf Services Reorder Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-reorder-pages-request-structure
- name: Adobe Pdf Services Replace Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-replace-pages-request-structure
- name: Adobe Pdf Services Rotate Pages Request Structure
  property_count: 2
  slug: adobe-pdf-services-rotate-pages-request-structure
- name: Adobe Pdf Services Split Pdf Request Structure
  property_count: 2
  slug: adobe-pdf-services-split-pdf-request-structure
- name: Adobe Structure
  property_count: 0
  slug: adobe-structure
jsonld:
- class_count: 45
  name: Adobe Context
  property_count: 51
  slug: adobe-context
- class_count: 0
  name: Adobe Pdf Services Context
  property_count: 0
  slug: adobe-pdf-services-context
layout: provider
mcp_servers:
- description: Adobe ships BOTH halves of an MCP surface. Six hosted remote HTTP endpoints across AEM Cloud, Adobe Analytics, Customer Journey Analytics and Creative Cloud answer JSON-RPC today (all auth-gated behin
  name: Adobe MCP servers (AEM, Analytics, CJA, Creative Cloud, Express)
  slug: adobe-mcp-servers-aem-analytics-cja-creative-cloud-express
- description: ''
  name: Adobe Express Developer MCP Server (local stdio)
  slug: adobe-express-developer-mcp-server-local-stdio
modified: '2026-08-13'
name: Adobe
nav: Providers
network: true
overview: 'Adobe publishes 52 APIs on the [APIs.io](https://apis.io/) network, including PDF Services Accessibility Auto-Tag API, PDF Services Assets API, PDF Services Combine PDF API, and 49 more. Tagged areas include E-Signature, Adobe, Fortune 1000, Analytics, and Creative Cloud.


  The Adobe catalog on APIs.io includes 1 event-driven AsyncAPI specification, 2 JSON-LD contexts, and 2 Spectral governance rulesets.


  Adobe''s developer surface includes sandbox, changelog, CLI, authentication, developer portal, documentation, API reference, and 70 more developer resources.'
plans:
- name: Adobe Plans Pricing
  plan_count: 5
  slug: adobe-plans-pricing
press:
- date: ''
  title: Adobe
  url: https://www.facebook.com/Adobe/
- date: ''
  title: Adobe Inc.
  url: https://en.wikipedia.org/wiki/Adobe_Inc.
- date: ''
  title: Adobe (@adobe) · San Jose, CA
  url: https://www.instagram.com/adobe/?hl=en
- date: ''
  title: 'Adobe: Creative, marketing and document management ...'
  url: https://www.adobe.com/
- date: ''
  title: Adobe (@Adobe) / Posts / X
  url: https://x.com/Adobe
random_paper: 1
rate_limits:
- limit_count: 10
  name: Adobe Rate Limits
  slug: adobe-rate-limits
rules:
- effective_rule_count: 6
  extends: []
  name: Adobe API Rules
  rule_count: 6
  severity_counts:
    error: 0
    hint: 0
    info: 2
    warn: 4
  slug: adobe-jsonschema-spectral-rules
- effective_rule_count: 59
  extends:
  - spectral:oas
  name: Adobe API Rules
  rule_count: 18
  severity_counts:
    error: 8
    hint: 0
    info: 1
    warn: 9
  slug: adobe-spectral-rules
score:
  band: exemplar
  composite: 80.9
  coverage:
    artifact_dirs: 38
    catalog_earned: 87.4
    catalog_earned_first_party: 24.0
    catalog_gap: 27.6
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.5
  facets:
    access_clarity: 100.0
    contract_governance: 45.5
    contract_quality: 67.9
    developer_ergonomics: 95.8
    discoverability: 71.7
    operational_transparency: 78.9
  previous_composite: 80.4
  provenance:
    agentic_access: derived
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 40
    mcp: first-party
    skills: first-party
  regulatory:
    applies: true
    matched_via: fallback
    regime: Horizontal (data, software, accessibility, platform)
    regime_id: horizontal
    score: 32.7
  schema_version: 0.23.0
  scored_at: '2026-10-03'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/adobe/refs/heads/main/screenshots/adobe-2026-07-25T181652.png
security:
- kind: authentication
  name: Adobe Authentication
  slug: adobe-authentication
  summary_line: http/apiKey/oauth2 · 3 schemes
- kind: domain-security
  name: Adobe Domain Security
  slug: adobe-domain-security
  summary_line: TLSv1.2 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Adobe Vulnerability Disclosure
  slug: adobe-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Adobe Trust Center
  slug: adobe-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, ISO 27018, PCI DSS, HIPAA, FedRAMP, CSA STAR, GDPR, C5 (Germany), IRAP (Australia), TISAX
slug: adobe
tags:
- E-Signature
- Adobe
- Fortune 1000
- Analytics
- Creative Cloud
- Digital Asset Management
- Document Services
- E-Commerce
- Experience Cloud
- Generative AI
- Marketing
- PDF
- Work Management
use_cases:
- Automating document workflows with PDF Services API
- Extracting data from invoices and forms with PDF Extract
- Generating creative assets at scale with Firefly API
- Embedding e-signature capabilities into business applications
- Building personalized customer experiences with Experience Platform
- Automating marketing campaigns and lead management
- Managing digital content and assets across channels
- Building and managing e-commerce storefronts
website: https://www.adobe.com/
---
