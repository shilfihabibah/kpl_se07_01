from enum import Enum

#State
class StudentStatusState(Enum):
    TERDAFTAR = "Terdaftar"
    CUTI = "Cuti"
    AKTIF = "Aktif"
    LULUS = "Lulus"

#Trigger Input
class TriggerInputState(Enum):
    CETAK_KSM = "Cetak KSM"
    MENYELESAIKAN_CUTI = "Menyelesaikan Cuti"
    LULUS = "Lulus"
    MENGAJUKAN_CUTI = "Mengajukan Cuti"

#Transision
state_transision =  {
    StudentStatusState.TERDAFTAR: {
        TriggerInputState.CETAK_KSM: StudentStatusState.AKTIF,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    },
    StudentStatusState.CUTI:{
        TriggerInputState.MENYELESAIKAN_CUTI: StudentStatusState.TERDAFTAR
    },
    StudentStatusState.AKTIF:{
        TriggerInputState.LULUS: StudentStatusState.LULUS,
        TriggerInputState.MENGAJUKAN_CUTI: StudentStatusState.CUTI
    }
}

def change_state(current_state, trigger_input) :
    cond_1 = current_state in state_transision #Return True or False
    cond_2 = trigger_input in state_transision[current_state] #Return True or False 
    if cond_1 and cond_2:
        #TERDAFTAR, AKTIF, LULUS, CUTI
        return state_transision[current_state] [trigger_input]
    return "Transisi Tidak Valid"

current_state = StudentStatusState.TERDAFTAR
trigger_input = TriggerInputState.LULUS

next_state = change_state(current_state, trigger_input)
print(next_state)
