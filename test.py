import Calculation_module.calculateOrder as Cal
import Calculation_module.initModel as initM


to=Cal.dfs_Search(initM.initData(5,5))
to.PrintDfsResult()
pass


# Cal.dfs_Search(initM.testData(2,2,[[1,0],[0,1]],[100,100],[[5,0],[0,6]],[[2,0],[0,3]],[[2,0],[0,2]])) 