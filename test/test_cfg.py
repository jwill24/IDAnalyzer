import FWCore.ParameterSet.Config as cms

process = cms.Process("analyzer")

process.load("FWCore.MessageService.MessageLogger_cfi")

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(100) )
process.MessageLogger.cerr.FwkReport.reportEvery = cms.untracked.int32(10)

process.source = cms.Source("PoolSource",
                            fileNames = cms.untracked.vstring(
                                'file:output_MiniAOD_4.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_4.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_5.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_2.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_49.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_50.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_18.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_44.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_47.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_45.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_46.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_48.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_21.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_3.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_1.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_43.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_40.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_42.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_41.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_39.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_36.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_38.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_35.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_33.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_37.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_6.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_20.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_17.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_7.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_13.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_26.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_30.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_34.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_12.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_22.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_16.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_25.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_32.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_19.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_24.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_23.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_28.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_10.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_29.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_31.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_14.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_15.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_27.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_9.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_11.root',
                                #'/store/group/phys_exotica/PPS-Diphoton/juwillia/GGtoGG_MiniAOD_zeta1_e-12_zeta2_0/190413_131300/0000/output_MiniAOD_8.root'
                        )
)

process.efficiency = cms.EDAnalyzer('IDAnalyzer',
                                    photons = cms.InputTag('slimmedPhotons')
                              )

process.p = cms.Path(process.efficiency)
