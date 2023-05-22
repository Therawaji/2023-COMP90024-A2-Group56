<template>
    <div class="title">
      <h3> View2 - Tweets by cities </h3>
    </div>
    <div class="life">
      <div ref="chart1" style="height: 600px;"></div>
      <ul>{{string}}</ul>
    </div>
</template>

<script>
import axios from 'axios';
import * as echarts from 'echarts';

export default {
    name: 'FirstView',
    props: {
        msg: String
    },
    data() {
        return {
            string: '# of tweets by cities',
            chart1: null,
            chart1Data: []
        };
    },
    methods: {
        async getData1() {
            try {
                const response = await axios.get('http://172.26.135.65:5000/view2');
                console.log(response.data);
                this.chart1Data = response.data;
                this.updateChart1();
            } catch (error) {
                console.log(error);
            }
        },
        updateChart1() {
            this.chart1.setOption(
                {
                  tooltip: {
                    trigger: 'item'
                  },
                  legend: {
                    top: '5%',
                    left: 'center'
                  },
                  series: [
                    {
                      name: 'Access From',
                      type: 'pie',
                      radius: ['40%', '70%'],
                      avoidLabelOverlap: false,
                      itemStyle: {
                        borderRadius: 10,
                        borderColor: '#fff',
                        borderWidth: 2
                      },
                      label: {
                        show: false,
                        position: 'center'
                      },
                      emphasis: {
                        label: {
                          show: true,
                          fontSize: 25,
                          fontWeight: 'bold'
                        }
                      },
                      labelLine: {
                        show: false
                      },
                      data: this.chart1Data
                    }
                  ]
                }
            );
        },
    },
    mounted() {
        this.chart1 = echarts.init(this.$refs.chart1);
        this.getData1();
    },
}
</script>

<style lang="scss" scoped>
template {
  size: 100%;
}
.title {
  margin-top: 40px;
}
</style>
