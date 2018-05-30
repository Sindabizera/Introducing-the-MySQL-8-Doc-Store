# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: contacts.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='contacts.proto',
  package='',
  syntax='proto2',
  serialized_pb=_b('\n\x0e\x63ontacts.proto\"w\n\x07\x43ontact\x12\r\n\x05\x66irst\x18\x01 \x02(\t\x12\n\n\x02id\x18\x02 \x02(\x05\x12\x0c\n\x04last\x18\x03 \x01(\t\x12$\n\x06phones\x18\x05 \x03(\x0b\x32\x14.Contact.PhoneNumber\x1a\x1d\n\x0bPhoneNumber\x12\x0e\n\x06number\x18\x01 \x02(\t\"\"\n\x08\x43ontacts\x12\x16\n\x04list\x18\x01 \x03(\x0b\x32\x08.Contact')
)
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CONTACT_PHONENUMBER = _descriptor.Descriptor(
  name='PhoneNumber',
  full_name='Contact.PhoneNumber',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='number', full_name='Contact.PhoneNumber.number', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=137,
)

_CONTACT = _descriptor.Descriptor(
  name='Contact',
  full_name='Contact',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first', full_name='Contact.first', index=0,
      number=1, type=9, cpp_type=9, label=2,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='id', full_name='Contact.id', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='last', full_name='Contact.last', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='phones', full_name='Contact.phones', index=3,
      number=5, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[_CONTACT_PHONENUMBER, ],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=18,
  serialized_end=137,
)


_CONTACTS = _descriptor.Descriptor(
  name='Contacts',
  full_name='Contacts',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='list', full_name='Contacts.list', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto2',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=139,
  serialized_end=173,
)

_CONTACT_PHONENUMBER.containing_type = _CONTACT
_CONTACT.fields_by_name['phones'].message_type = _CONTACT_PHONENUMBER
_CONTACTS.fields_by_name['list'].message_type = _CONTACT
DESCRIPTOR.message_types_by_name['Contact'] = _CONTACT
DESCRIPTOR.message_types_by_name['Contacts'] = _CONTACTS

Contact = _reflection.GeneratedProtocolMessageType('Contact', (_message.Message,), dict(

  PhoneNumber = _reflection.GeneratedProtocolMessageType('PhoneNumber', (_message.Message,), dict(
    DESCRIPTOR = _CONTACT_PHONENUMBER,
    __module__ = 'contacts_pb2'
    # @@protoc_insertion_point(class_scope:Contact.PhoneNumber)
    ))
  ,
  DESCRIPTOR = _CONTACT,
  __module__ = 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:Contact)
  ))
_sym_db.RegisterMessage(Contact)
_sym_db.RegisterMessage(Contact.PhoneNumber)

Contacts = _reflection.GeneratedProtocolMessageType('Contacts', (_message.Message,), dict(
  DESCRIPTOR = _CONTACTS,
  __module__ = 'contacts_pb2'
  # @@protoc_insertion_point(class_scope:Contacts)
  ))
_sym_db.RegisterMessage(Contacts)


# @@protoc_insertion_point(module_scope)