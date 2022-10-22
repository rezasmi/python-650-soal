while True:
    vam=int(input('vam darkhasti: '))
    tedad_qest=int(input('tedad qest: '))
    mablaq_bahre=int(input('bahre: '))
    mablaq=(12*vam)*(12-tedad_qest*mablaq_bahre/100)
    pardakhti_vam=mablaq/tedad_qest
    print('mablagh_pardakhti= ',mablaq,'\t', pardakhti_vam)
    answer_is=input('mikhay edame bedi?(y/n) ')
    if answer_is=='n':
        break
    