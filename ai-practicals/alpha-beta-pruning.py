tree=[[5,4,5],[6,7,5],[6,7,8],[-9,-8,7]]
root=0
pruned=0


def alphaBeta(branch,depth,alpha,beta):
    global pruned
    i=0
    for child in branch:
        if(isinstance(child,list)):
            nextAlpha,nextBeta=alphaBeta(child,depth+1,alpha,beta)
           
            if depth%2==0:
                alpha=max(alpha,nextBeta)
            else:
                beta=min(beta,nextAlpha)
               
            branch[i]=alpha if depth%2==0 else beta
            i+=1;
           
        else:
            if depth%2==0:
                alpha=max(alpha,child)
            else:
                beta=min(beta,child)
               
            if(alpha>=beta):
                pruned+=1
                break


    return  alpha,beta




alpha,beta = alphaBeta(tree,root,-15,15)


print(f"alpha: {alpha} beta:{beta}")
print(f"pruned:{pruned}")
