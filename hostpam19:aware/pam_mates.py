# -*-coding: utf-8-*-
# pam_mates.py
# Validar l'usuari realitzant una pregunta de matematiques facil

def pam_sm_authenticate (pamh, flags, argv):
  print "Quant fan 2*5?"
  resposta=raw_input()
  if int(resposta) == 10:
    return pamh.PAM_SUCCESS
  else:
    return pamh.PAM_AUTHTOK_ERR

def pam_sm_setcred (pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_acct_mgmt (pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_open_session (pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_close_session (pamh, flags, argv):
  return pamh.PAM_SUCCESS

def pam_sm_chauthtok (pamh, flags, argv):
  return pamh.PAM_SUCCESS

