a=float(input('delta_t:'))
b=float(input('s_0:'))

def moto_rett_unif(delta_t,s_0):
  v=10
  s=s_0+v*delta_t
  return s

def moto_accelerato(delta_t,s_0):
  v_0=10
  a=1
  s=s_0+v_0*delta_t+0.5*a*delta_t**2
  return s

print('moto_rett_unif:', moto_rett_unif(a,b))

print('moto_accelerato:', moto_accelerato(a,b))