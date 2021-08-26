import re

HEAD = 'HEAD'
TEMP = '--TEMP--'

NAMESPACE_PATTERN = r'[a-zA-Z0-9\-\.\_\@]+'
NAMESPACE_REGEX = re.compile(r'^' + NAMESPACE_PATTERN + '$')

ACCESS_TYPE_VIEW = 'View'
ACCESS_TYPE_EDIT = 'Edit'
ACCESS_TYPE_NONE = 'None'
DEFAULT_ACCESS_TYPE = ACCESS_TYPE_VIEW
ACCESS_TYPE_CHOICES = ((ACCESS_TYPE_VIEW, 'View'),
                       (ACCESS_TYPE_EDIT, 'Edit'),
                       (ACCESS_TYPE_NONE, 'None'))
SUPER_ADMIN_USER_ID = 1
OCL_ORG_ID = 1
VERBOSE_PARAM = 'verbose'
BRIEF_PARAM = 'brief'
UPDATED_SINCE_PARAM = 'updatedSince'
LAST_LOGIN_SINCE_PARAM = 'lastLoginSince'
LAST_LOGIN_BEFORE_PARAM = 'lastLoginBefore'
DATE_JOINED_SINCE_PARAM = 'dateJoinedSince'
DATE_JOINED_BEFORE_PARAM = 'dateJoinedBefore'
RELEASED_PARAM = 'released'
PROCESSING_PARAM = 'processing'
ISO_639_1 = 'ISO 639-1'
NA = 'n/a'
YES = 'yes'
NO = 'no'
CUSTOM_VALIDATION_SCHEMA_OPENMRS = 'OpenMRS'
LOOKUP_CONCEPT_CLASSES = ['Concept Class', 'Datatype', 'NameType', 'DescriptionType', 'MapType', 'Locale']
LOOKUP_SOURCES = ['Classes', 'Datatypes', 'NameTypes', 'DescriptionTypes', 'MapTypes', 'Locales']
REFERENCE_VALUE_SOURCE_MNEMONICS = ['Classes', 'Datatypes', 'NameTypes', 'DescriptionTypes', 'Locales']
FIVE_MINS = 5 * 60
DEFAULT_REPOSITORY_TYPE = 'Collection'
OPENMRS_REPOSITORY_TYPE = 'OpenMRSDictionary'
INCLUDE_RETIRED_PARAM = 'includeRetired'
INCLUDE_MAPPINGS_PARAM = 'includeMappings'
INCLUDE_EXTRAS_PARAM = 'includeExtras'
INCLUDE_PARENT_CONCEPTS = 'includeParentConcepts'
INCLUDE_CHILD_CONCEPTS = 'includeChildConcepts'
INCLUDE_HIERARCHY_PATH = 'includeHierarchyPath'
INCLUDE_PARENT_CONCEPT_URLS = 'includeParentConceptURLs'
INCLUDE_CHILD_CONCEPT_URLS = 'includeChildConceptURLs'
INCLUDE_INVERSE_MAPPINGS_PARAM = 'includeInverseMappings'
INCLUDE_SUBSCRIBED_ORGS = 'includeSubscribedOrgs'
INCLUDE_CLIENT_CONFIGS = 'includeClientConfigs'
INCLUDE_HIERARCHY_ROOT = 'includeHierarchyRoot'
INCLUDE_SUMMARY = 'includeSummary'
INCLUDE_VERIFICATION_TOKEN = 'includeVerificationToken'
INCLUDE_AUTH_GROUPS = 'includeAuthGroups'
INCLUDE_SOURCE_VERSIONS = 'includeSourceVersions'
INCLUDE_COLLECTION_VERSIONS = 'includeCollectionVersions'
MAPPING_LOOKUP_CONCEPTS = 'lookupConcepts'
MAPPING_LOOKUP_FROM_CONCEPT = 'lookupFromConcept'
MAPPING_LOOKUP_TO_CONCEPT = 'lookupToConcept'
MAPPING_LOOKUP_SOURCES = 'lookupSources'
MAPPING_LOOKUP_FROM_SOURCE = 'lookupFromSource'
MAPPING_LOOKUP_TO_SOURCE = 'lookupToSource'
LIMIT_PARAM = 'limit'
LOOKUP_ATTRIBUTES_MUST_BE_IMPORTED = 'Lookup attributes must be imported'
LIST_DEFAULT_LIMIT = 25
CSV_DEFAULT_LIMIT = 1000
SEARCH_PARAM = 'q'
INCLUDE_FACETS = 'HTTP_INCLUDEFACETS'
FACETS_ONLY = 'facetsOnly'
HTTP_COMPRESS_HEADER = 'HTTP_COMPRESS'
NOT_FOUND = 'Not found.'
OK_MESSAGE = 'ok!'
PERSIST_NEW_ERROR_MESSAGE = "An error occurred while trying to persist new {}."
MUST_SPECIFY_EXTRA_PARAM_IN_BODY = 'Must specify {} param in body.'
SOURCE_PARENT_CANNOT_BE_NONE = 'Source parent cannot be None.'
PARENT_RESOURCE_CANNOT_BE_NONE = 'Parent resource cannot be None.'
CREATOR_CANNOT_BE_NONE = 'Creator cannot be None.'
CANNOT_DELETE_ONLY_VERSION = 'Cannot delete only version.'
BULK_IMPORT_QUEUES_COUNT = 4
MAX_PINS_ALLOWED = 4
CONFIRM_EMAIL_ADDRESS_MAIL_SUBJECT = "Confirm E-mail Address"
PASSWORD_RESET_MAIL_SUBJECT = "Password Reset E-mail"
LATEST = 'latest'
VERSION_HEADER = 'X-OCL-API-VERSION'
CREATE_PARENT_VERSION_QUERY_PARAM = 'createParentVersion'
